
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QObject, QIODevice, Slot, Signal
from .protobuf import *
from typing import *
from crc import Calculator, Crc16
from dataclasses import dataclass
import logging

LOG = logging.getLogger(f"{__name__}")
LOG.setLevel(logging.DEBUG)

MAX_MSG_SIZE = 64
FRAME_START_MARKER = 0x7E

START_FIELD_POS = 0
TYPE_FIELD_POS = 1
LENGTH_FIELD_POS = 2
DATA_FIELD_POS = 3

class FilamuxClient(QObject):
    """
    Signals:
        connected()
        disconnected(reason: str)
    Slots:
        sendExtruderGcode(gcode: str)
        sendSetSpoolParams(index: int, length: int)
        sendSetTargetSpool(spool: int)
    """

    connected = Signal()
    disconnected = Signal(str)

    def __init__(self):
        super().__init__()
        self._connected = False
        self._port = QSerialPort()
        self._port.setBaudRate(QSerialPort.BaudRate.Baud115200)
        self._port.setDataBits(QSerialPort.DataBits.Data8)
        self._port.setParity(QSerialPort.Parity.NoParity)
        self._port.setStopBits(QSerialPort.StopBits.OneStop)
        self._port.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
        self._port.readyRead.connect(self._readData)
        self._transactionOngoing = False
        self._rxBuffer = []
        self._bytesRemaining = 0

        self._frameQueue = []

    def isConnected(self):
        return self._port.isOpen()

    def setBaudRate(self, baud: QSerialPort.BaudRate):
        self._port.baudRate = baud

    def setPort(self, port: str):
        self._port.setPortName(port)

    def start(self):
        self._port.open(QIODevice.ReadWrite)
        if self.isConnected():
            LOG.info("Connected")
            self.connected.emit()
        else:
            msg = f"Nie połączono: {self._port.errorString()}"
            LOG.error(msg)
            self.disconnected.emit(msg)

    def process(self):
        pass

    def stop(self):
        self._port.close()

    def _sendData(self, messageType: MessageType, data: bytearray):
        frame = bytearray()
        frame.append(0x7E)
        frame.append(messageType)
        frame.append(len(data) + 2) # account for CRC
        frame += data

        calc = Calculator(Crc16.KERMIT)
        crc = calc.checksum(data)

        frame.append((crc>>8) & 0xFF)
        frame.append(crc & 0xFF)

        if not self._transactionOngoing:
            self._transactionOngoing = True
            self._port.write(frame)
        elif len(self._frameQueue) < 5:
            LOG.debug(f"Moving frame {MessageType.Name(messageType)} to queue. Queue len: {len(self._frameQueue)}")
            self._frameQueue.append(frame)
        else:
            LOG.critical("Frame queue exceeded. Dropping frame")

    @Slot(str)
    def sendExtruderGcode(self, gcode: str):
        frame = ExtruderGCodeReq(gcode=gcode)
        self._sendData(MessageType.MSG_EXTRUDER_GCODE, frame.SerializeToString())

    @Slot(int)
    def sendSetSpoolParams(self, index: int, length: int):
        req = SetSpoolParamsReq(index=index, length=length)
        data = req.SerializeToString()
        self._sendData(MessageType.MSG_SET_SPOOL_PARAMS, data)

    @Slot(int)
    def sendSetTargetSpool(self, spool: int):
        req = SetTargetSpoolReq(index=spool)
        data = req.SerializeToString()
        self._sendData(MessageType.MSG_SET_TARGET_SPOOL, data)

    def _handleSetTargetSpoolRes(self, payload: bytes):
        res = SetTargetSpoolRes.FromString(payload)
        if not res.IsInitialized():
            LOG.error(f"Cannot parse SetTargetSpoolRes: {payload}")
            return
        if res.ok:
            LOG.info("Set target spool: OK")
        else:
            LOG.error(f"Set target spool error. {res.reason if res.reason is not None else ''}")

    def _handleSetSpoolParams(self, payload: bytes):
        res = SetSpoolParamsRes.FromString(payload)
        if not res.IsInitialized():
            LOG.error(f"Cannot parse SetSpoolParamsRes: {payload}")
            return
        if res.ok:
            LOG.info("Set spool params: OK")
        else:
            LOG.error(f"Set spool params error. {res.reason if res.reason is not None else ''}")

    def _getPayload(self, buffer: List[int]) -> bytes:
        length = buffer[LENGTH_FIELD_POS]
        payload = buffer[DATA_FIELD_POS:DATA_FIELD_POS+length]
        return bytes(payload)

    def _processRxBuffer(self):
        if len(self._rxBuffer) <= DATA_FIELD_POS:
            return 

        length = self._rxBuffer[LENGTH_FIELD_POS]
        if len(self._rxBuffer) < length + DATA_FIELD_POS + 2:
            # Wait for rest of frame
            return
        if len(self._rxBuffer) > length + DATA_FIELD_POS + 2:
            LOG.error("rx buffer exceeded expected length. Dropping")
            self._rxBuffer = []
            return

        frameType = MessageType.Name(self._rxBuffer[TYPE_FIELD_POS])

        LOG.info(f"Frame type: {frameType}")
        if frameType == "MSG_SET_TARGET_SPOOL":
            self._handleSetTargetSpoolRes(self._getPayload(self._rxBuffer))
        self._transactionOngoing = False
        self._rxBuffer = []

    @Slot()
    def _readData(self):
        data = self._port.readAll()
        LOG.debug(f"Received: {data}")

        # Process received data
        for b in data.data():
            if len(self._rxBuffer) == 0:
                # Look for start frame marker
                if b != FRAME_START_MARKER:
                    continue
            self._rxBuffer.append(b)
            self._processRxBuffer()

        # Process queue
        if not self._transactionOngoing and len(self._frameQueue) > 0:
            self._transactionOngoing = True
            self._port.write(self._frameQueue.pop())

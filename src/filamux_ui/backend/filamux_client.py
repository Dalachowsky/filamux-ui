
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QIODevice, Slot, Signal
from .protobuf import *
from crc import Calculator, Crc16

class FilamuxClient:

    def __init__(self):
        self._connected = False
        self._port = QSerialPort()
        self._transactionOngoing = False

    def isConnected(self):
        return self._port.isConnected()

    def setBaudRate(self, baud: QSerialPort.BaudRate):
        self._port.baudRate = baud

    def setPort(self, port: str):
        self._port.setPortName(port)

    def start(self):
        self._port.open(QIODevice.OpenModeFlag.ReadWrite)

    def process(self):
        pass

    def stop(self):
        self._port.close()

    def _sendData(self, messageType: MessageType, data: bytearray):
        frame = bytearray()
        frame.append(0x7E)
        frame.append(messageType)
        frame.append(data.count())
        frame.append(data)

        calc = Calculator(Crc16.KERMIT)
        crc = calc.checksum(data)

        frame.append((crc>>8) & 0xFF)
        frame.append(crc & 0xFF)

        self._port.write(frame)

    @Slot(int)
    def sendSetActiveSpool(self, spool: int):
        req = SetTargetSpoolReq(index=spool)
        data = req.SerializeToString()
        self._sendData(MessageType.MSG_SET_TARGET_SPOOL, data)

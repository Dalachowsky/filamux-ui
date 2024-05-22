
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QIODevice
from .protobuf import *

class FilamuxClient:

    def __init__(self):
        self._connected = False
        self._port = QSerialPort()

    def isConnected(self):
        return self._port.isConnected()

    def setBaudRate(self, baud: QSerialPort.BaudRate):
        self._port.baudRate = baud

    def setPort(self, port: str):
        self._port.setPortName(port)

    def start(self):
        self._port.open(QIODevice.OpenModeFlag.ReadWrite)

    def stop(self):
        self._port.close()

from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import QRectF

class NetworkDevice(QGraphicsItem):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def boundingRect(self):
        return QRectF(0, 0, 50, 50)

    def paint(self, painter, option, widget):
        painter.setBrush(QBrush(QColor(100, 100, 150)))
        painter.drawRect(0, 0, 50, 50)

class Router(NetworkDevice):
    def __init__(self, name):
        super().__init__(name)

class Switch(NetworkDevice):
    def __init__(self, name):
        super().__init__(name)

class Host(NetworkDevice):
    def __init__(self, name):
        super().__init__(name)

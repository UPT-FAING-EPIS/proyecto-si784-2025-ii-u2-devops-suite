import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsView, QGraphicsScene

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from network_simulator.devices import Router, Switch, Host

class NetworkSimulatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        # Controles
        controls_layout = QVBoxLayout()
        self.add_router_button = QPushButton("Añadir Router")
        self.add_switch_button = QPushButton("Añadir Switch")
        self.add_host_button = QPushButton("Añadir Host")
        controls_layout.addWidget(self.add_router_button)
        controls_layout.addWidget(self.add_switch_button)
        controls_layout.addWidget(self.add_host_button)
        self.layout.addLayout(controls_layout)

        # Lienzo
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.layout.addWidget(self.view)

        # Conexiones
        self.add_router_button.clicked.connect(lambda: self.add_device(Router, "Router"))
        self.add_switch_button.clicked.connect(lambda: self.add_device(Switch, "Switch"))
        self.add_host_button.clicked.connect(lambda: self.add_device(Host, "Host"))

        self.device_count = 0

    def add_device(self, device_class, name_prefix):
        self.device_count += 1
        device_name = f"{name_prefix}_{self.device_count}"
        device = device_class(device_name)
        self.scene.addItem(device)

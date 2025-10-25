import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from cloud_deployment.deployer import Deployer

class CloudDeploymentUI(QWidget):
    def __init__(self):
        super().__init__()
        self.deployer = Deployer()
        self.layout = QVBoxLayout(self)

        # Entradas
        input_layout = QVBoxLayout()
        self.provider_label = QLabel("Proveedor de la Nube:")
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(["AWS", "Azure", "Google Cloud"])
        input_layout.addWidget(self.provider_label)
        input_layout.addWidget(self.provider_combo)

        self.app_name_label = QLabel("Nombre de la Aplicación:")
        self.app_name_input = QLineEdit()
        input_layout.addWidget(self.app_name_label)
        input_layout.addWidget(self.app_name_input)

        self.region_label = QLabel("Región:")
        self.region_input = QLineEdit()
        input_layout.addWidget(self.region_label)
        input_layout.addWidget(self.region_input)

        self.deploy_button = QPushButton("Desplegar")
        self.deploy_button.clicked.connect(self.deploy)

        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.deploy_button)

    def deploy(self):
        provider = self.provider_combo.currentText()
        config = {
            "app_name": self.app_name_input.text(),
            "region": self.region_input.text()
        }
        self.deployer.deploy(provider, config)

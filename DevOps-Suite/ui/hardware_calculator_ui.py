import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from hardware_calculator.calculator import HardwareCalculator

class HardwareCalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = HardwareCalculator()
        self.layout = QVBoxLayout(self)

        # Entradas
        input_layout = QHBoxLayout()
        self.app_type_label = QLabel("Tipo de Aplicación:")
        self.app_type_combo = QComboBox()
        self.app_type_combo.addItems(["Web App", "Database", "Other"])
        input_layout.addWidget(self.app_type_label)
        input_layout.addWidget(self.app_type_combo)

        self.user_load_label = QLabel("Carga de Usuarios:")
        self.user_load_spinbox = QSpinBox()
        self.user_load_spinbox.setRange(1, 10000)
        input_layout.addWidget(self.user_load_label)
        input_layout.addWidget(self.user_load_spinbox)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_requirements)

        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.calculate_button)

        # Resultados
        self.cpu_result_label = QLabel("CPU Recomendada: N/A")
        self.ram_result_label = QLabel("RAM Recomendada: N/A")
        self.disk_result_label = QLabel("Disco Recomendado: N/A")
        self.layout.addWidget(self.cpu_result_label)
        self.layout.addWidget(self.ram_result_label)
        self.layout.addWidget(self.disk_result_label)

    def calculate_requirements(self):
        app_type = self.app_type_combo.currentText()
        user_load = self.user_load_spinbox.value()

        requirements = self.calculator.calculate_requirements(app_type, user_load)

        self.cpu_result_label.setText(f"CPU Recomendada: {requirements['cpu']}")
        self.ram_result_label.setText(f"RAM Recomendada: {requirements['ram']}")
        self.disk_result_label.setText(f"Disco Recomendado: {requirements['disk']}")

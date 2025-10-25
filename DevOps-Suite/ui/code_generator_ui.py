import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, QTextEdit, QLabel
from code_generator.generator import CodeGenerator

class CodeGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Pattern selection
        pattern_layout = QHBoxLayout()
        pattern_label = QLabel("Patrón:")
        self.pattern_combo = QComboBox()
        self.pattern_combo.addItems(["Singleton"])
        pattern_layout.addWidget(pattern_label)
        pattern_layout.addWidget(self.pattern_combo)
        layout.addLayout(pattern_layout)

        # Class name input
        class_name_layout = QHBoxLayout()
        class_name_label = QLabel("Nombre de la Clase:")
        self.class_name_input = QLineEdit()
        class_name_layout.addWidget(class_name_label)
        class_name_layout.addWidget(self.class_name_input)
        layout.addLayout(class_name_layout)

        # Generate button
        self.generate_button = QPushButton("Generar Código")
        self.generate_button.clicked.connect(self.generate_code)
        layout.addWidget(self.generate_button)

        # Generated code display
        self.code_display = QTextEdit()
        self.code_display.setReadOnly(True)
        layout.addWidget(self.code_display)

        self.setLayout(layout)
        self.code_generator = CodeGenerator()

    def generate_code(self):
        pattern = self.pattern_combo.currentText()
        class_name = self.class_name_input.text()

        if not class_name:
            self.code_display.setText("Por favor, introduce un nombre de clase.")
            return

        if pattern == "Singleton":
            code = self.code_generator.generate_singleton(class_name)
            self.code_display.setText(code)

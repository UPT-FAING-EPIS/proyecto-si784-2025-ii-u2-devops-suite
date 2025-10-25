import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit, QPushButton, QLabel
from syntax_validator.validator import SyntaxValidator

class SyntaxValidatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Language selection
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Lenguaje:")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Python", "C#", "Java"])
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # Code input
        self.code_input = QTextEdit()
        layout.addWidget(self.code_input)

        # Validate button
        self.validate_button = QPushButton("Validar Sintaxis")
        self.validate_button.clicked.connect(self.validate_syntax)
        layout.addWidget(self.validate_button)

        # Result display
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.validator = SyntaxValidator()

    def validate_syntax(self):
        lang = self.lang_combo.currentText()
        code = self.code_input.toPlainText()

        if not code:
            self.result_label.setText("Por favor, introduce código para validar.")
            return

        if lang == "Python":
            is_valid, error = self.validator.validate_python(code)
        elif lang == "C#":
            is_valid, error = self.validator.validate_csharp(code)
        elif lang == "Java":
            is_valid, error = self.validator.validate_java(code)

        if is_valid:
            self.result_label.setText("Sintaxis válida.")
        else:
            self.result_label.setText(f"Error de sintaxis: {error}")

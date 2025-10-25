import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit, QPushButton, QLabel
from data_converter.converter import DataConverter

class DataConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Format selection
        format_layout = QHBoxLayout()
        self.from_combo = QComboBox()
        self.from_combo.addItems(["JSON", "XML"])
        self.to_combo = QComboBox()
        self.to_combo.addItems(["XML", "JSON"])
        format_layout.addWidget(QLabel("De:"))
        format_layout.addWidget(self.from_combo)
        format_layout.addWidget(QLabel("A:"))
        format_layout.addWidget(self.to_combo)
        layout.addLayout(format_layout)

        # Input and output
        io_layout = QHBoxLayout()
        self.input_text = QTextEdit()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        io_layout.addWidget(self.input_text)
        io_layout.addWidget(self.output_text)
        layout.addLayout(io_layout)

        # Convert button
        self.convert_button = QPushButton("Convertir")
        self.convert_button.clicked.connect(self.convert_data)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.converter = DataConverter()

    def convert_data(self):
        from_format = self.from_combo.currentText()
        to_format = self.to_combo.currentText()
        input_data = self.input_text.toPlainText()

        if not input_data:
            self.output_text.setText("Por favor, introduce datos para convertir.")
            return

        if from_format == to_format:
            self.output_text.setText("Los formatos de entrada y salida no pueden ser los mismos.")
            return

        if from_format == "JSON" and to_format == "XML":
            output_data, error = self.converter.json_to_xml(input_data)
        elif from_format == "XML" and to_format == "JSON":
            output_data, error = self.converter.xml_to_json(input_data)
        else:
            self.output_text.setText("Conversión no soportada.")
            return

        if error:
            self.output_text.setText(f"Error: {error}")
        else:
            self.output_text.setText(output_data)

import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from reporting.report_generator import ReportGenerator

class ReportsUI(QWidget):
    def __init__(self, metrics_collector):
        super().__init__()
        self.metrics_collector = metrics_collector
        self.layout = QVBoxLayout(self)

        self.generate_button = QPushButton("Generar Reporte")
        self.generate_button.clicked.connect(self.generate_report)
        self.layout.addWidget(self.generate_button)

    def generate_report(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar Reporte", "", "PDF Files (*.pdf)")
        if filename:
            metrics = self.metrics_collector.get_latest_metrics()
            data = {
                "Uso de CPU": f"{metrics.get('cpu', 'N/A'):.2f}%",
                "Uso de Memoria": f"{metrics.get('mem', 'N/A'):.2f}%",
                "Uso de Disco": f"{metrics.get('disk', 'N/A'):.2f}%",
                "Bytes Enviados": f"{metrics.get('net_sent', 0)/1024/1024:.2f} MB",
                "Bytes Recibidos": f"{metrics.get('net_recv', 0)/1024/1024:.2f} MB"
            }
            generator = ReportGenerator(filename)
            generator.generate_report(data)
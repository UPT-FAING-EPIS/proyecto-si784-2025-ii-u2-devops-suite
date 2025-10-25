import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from monitoring.metrics_collector import MetricsCollector

class MetricsUI(QWidget):
    def __init__(self, metrics_collector, alert_manager):
        super().__init__()
        self.metrics_collector = metrics_collector
        self.alert_manager = alert_manager
        self.layout = QVBoxLayout(self)

        self.cpu_label = QLabel("CPU Usage: N/A")
        self.mem_label = QLabel("Memory Usage: N/A")
        self.disk_label = QLabel("Disk Usage: N/A")
        self.net_label = QLabel("Network Usage: N/A")

        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.mem_label)
        self.layout.addWidget(self.disk_label)
        self.layout.addWidget(self.net_label)

        self.alert_manager.alert_triggered.connect(self.show_alert)

        self.start_monitoring()

    def start_monitoring(self):
        self.thread = QThread()
        self.collector = self.metrics_collector
        self.collector.moveToThread(self.thread)

        self.thread.started.connect(self.collector.run)
        self.collector.metrics_updated.connect(self.update_metrics)
        self.collector.metrics_updated.connect(self.alert_manager.check_metrics)

        self.thread.start()

    def update_metrics(self, metrics):
        self.cpu_label.setText(f"CPU Usage: {metrics['cpu']:.2f}%")
        self.mem_label.setText(f"Memory Usage: {metrics['mem']:.2f}%")
        self.disk_label.setText(f"Disk Usage: {metrics['disk']:.2f}%")
        self.net_label.setText(f"Network Usage: Sent={metrics['net_sent']/1024/1024:.2f} MB, Recv={metrics['net_recv']/1024/1024:.2f} MB")

    def show_alert(self, message):
        print(message)
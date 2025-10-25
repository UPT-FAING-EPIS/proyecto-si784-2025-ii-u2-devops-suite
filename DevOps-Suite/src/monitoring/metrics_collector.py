import psutil
import time
from PyQt5.QtCore import QObject, pyqtSignal

class MetricsCollector(QObject):
    metrics_updated = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self._is_running = True
        self.latest_metrics = {}

    def run(self):
        while self._is_running:
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent
            net_io = psutil.net_io_counters()
            
            self.latest_metrics = {
                "cpu": cpu_usage,
                "mem": mem_usage,
                "disk": disk_usage,
                "net_sent": net_io.bytes_sent,
                "net_recv": net_io.bytes_recv
            }
            self.metrics_updated.emit(self.latest_metrics)
            time.sleep(1)

    def stop(self):
        self._is_running = False

    def get_latest_metrics(self):
        return self.latest_metrics
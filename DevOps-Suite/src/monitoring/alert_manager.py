from PyQt5.QtCore import QObject, pyqtSignal

class AlertRule:
    def __init__(self, metric, threshold):
        self.metric = metric
        self.threshold = threshold

class AlertManager(QObject):
    alert_triggered = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def check_metrics(self, metrics):
        for rule in self.rules:
            if rule.metric in metrics and metrics[rule.metric] > rule.threshold:
                self.alert_triggered.emit(f"Alerta: {rule.metric} ha superado el umbral de {rule.threshold}%")

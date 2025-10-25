import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from monitoring.alert_manager import AlertRule

class AlertsUI(QWidget):
    def __init__(self, alert_manager):
        super().__init__()
        self.alert_manager = alert_manager
        self.layout = QVBoxLayout(self)

        self.rule_label = QLabel("Nueva Regla de Alerta:")
        self.layout.addWidget(self.rule_label)

        self.metric_input = QLineEdit()
        self.metric_input.setPlaceholderText("Métrica (cpu, mem, disk)")
        self.layout.addWidget(self.metric_input)

        self.threshold_input = QLineEdit()
        self.threshold_input.setPlaceholderText("Umbral (%)")
        self.layout.addWidget(self.threshold_input)

        self.add_rule_button = QPushButton("Añadir Regla")
        self.add_rule_button.clicked.connect(self.add_rule)
        self.layout.addWidget(self.add_rule_button)

        self.rules_list = QListWidget()
        self.layout.addWidget(self.rules_list)

    def add_rule(self):
        metric = self.metric_input.text()
        try:
            threshold = float(self.threshold_input.text())
            rule = AlertRule(metric, threshold)
            self.alert_manager.add_rule(rule)
            self.update_rules_list()
        except ValueError:
            print("El umbral debe ser un número.")

    def update_rules_list(self):
        self.rules_list.clear()
        for rule in self.alert_manager.rules:
            self.rules_list.addItem(f"Métrica: {rule.metric}, Umbral: {rule.threshold}%")
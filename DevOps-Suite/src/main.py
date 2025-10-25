import sys
import os

try:
    # Running as a PyInstaller bundle
    base_path = sys._MEIPASS
    # Add the 'ui' folder and the root of the bundle to the path
    sys.path.append(os.path.join(base_path, 'ui'))
    sys.path.append(base_path)
except Exception:
    # Running as a normal script
    # The script is in 'src', so we go up one level to the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Add 'src' and 'ui' folders to the path
    sys.path.append(os.path.join(project_root, 'src'))
    sys.path.append(os.path.join(project_root, 'ui'))

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtGui import QIcon
from automation_ui import AutomationUI
from metrics_ui import MetricsUI
from alerts_ui import AlertsUI
from reports_ui import ReportsUI
from network_simulator_ui import NetworkSimulatorUI
from hardware_calculator_ui import HardwareCalculatorUI
from cloud_deployment_ui import CloudDeploymentUI
from code_generator_ui import CodeGeneratorUI
from syntax_validator_ui import SyntaxValidatorUI
from data_converter_ui import DataConverterUI
from monitoring.alert_manager import AlertManager
from monitoring.metrics_collector import MetricsCollector

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DevOps-Suite")
        
        # Determine the correct path for the icon
        if hasattr(sys, '_MEIPASS'):
            # Running as a PyInstaller bundle
            base_path = sys._MEIPASS
        else:
            # Running as a normal script
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        icon_path = os.path.join(base_path, "resources", "logo.png")
        self.setWindowIcon(QIcon(icon_path))

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        alert_manager = AlertManager()
        metrics_collector = MetricsCollector()

        self.automation_tab = AutomationUI()
        self.monitoring_tab = MetricsUI(metrics_collector, alert_manager)
        self.alerts_tab = AlertsUI(alert_manager)
        self.reports_tab = ReportsUI(metrics_collector)
        self.network_simulator_tab = NetworkSimulatorUI()
        self.hardware_calculator_tab = HardwareCalculatorUI()
        self.cloud_deployment_tab = CloudDeploymentUI()
        self.code_generator_tab = CodeGeneratorUI()
        self.syntax_validator_tab = SyntaxValidatorUI()
        self.data_converter_tab = DataConverterUI()

        self.tabs.addTab(self.automation_tab, "Automatización")
        self.tabs.addTab(self.monitoring_tab, "Monitorización")
        self.tabs.addTab(self.alerts_tab, "Alertas")
        self.tabs.addTab(self.reports_tab, "Reportes")
        self.tabs.addTab(self.network_simulator_tab, "Simulador de Red")
        self.tabs.addTab(self.hardware_calculator_tab, "Calculadora de Hardware")
        self.tabs.addTab(self.cloud_deployment_tab, "Despliegue en la Nube")
        self.tabs.addTab(self.code_generator_tab, "Generador de Código")
        self.tabs.addTab(self.syntax_validator_tab, "Validador de Sintaxis")
        self.tabs.addTab(self.data_converter_tab, "Convertidor de Datos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QGroupBox, QFormLayout, QHeaderView

# Este módulo define los componentes principales de la interfaz de usuario.
class MainUI(QWidget):
    # Constructor que crea y organiza los widgets de la interfaz de usuario.
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Sección de gestión de proyectos
        self.project_group = QGroupBox("Proyectos")
        self.project_layout = QFormLayout()
        self.project_combo = QComboBox()
        self.new_project_button = QPushButton("Nuevo Proyecto")
        self.project_layout.addRow(QLabel("Seleccionar Proyecto:"), self.project_combo)
        self.project_layout.addRow(self.new_project_button)
        self.project_group.setLayout(self.project_layout)
        self.layout.addWidget(self.project_group)

        # Sección de gestión de casos de prueba
        self.test_case_group = QGroupBox("Casos de Prueba")
        self.test_case_layout = QVBoxLayout()
        self.test_case_table = QTableWidget()
        self.test_case_table.setColumnCount(5)
        self.test_case_table.setHorizontalHeaderLabels(["ID", "Nombre", "Prioridad", "Estado", "Resultado"])
        self.test_case_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.button_layout = QHBoxLayout()
        self.new_test_case_button = QPushButton("Nuevo Caso de Prueba")
        self.execute_test_button = QPushButton("Ejecutar Prueba")
        self.report_button = QPushButton("Generar Informe")
        self.button_layout.addWidget(self.new_test_case_button)
        self.button_layout.addWidget(self.execute_test_button)
        self.button_layout.addWidget(self.report_button)
        self.test_case_layout.addWidget(self.test_case_table)
        self.test_case_layout.addLayout(self.button_layout)
        self.test_case_group.setLayout(self.test_case_layout)
        self.layout.addWidget(self.test_case_group)
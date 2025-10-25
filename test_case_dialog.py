from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QTextEdit, QComboBox, QPushButton, QDialogButtonBox

# Este módulo define el diálogo para crear y editar casos de prueba.
class TestCaseDialog(QDialog):
    # Constructor que crea el diálogo para los casos de prueba.
    def __init__(self, test_case=None):
        super().__init__()
        self.setWindowTitle("Caso de Prueba")
        self.layout = QFormLayout(self)

        self.name_edit = QLineEdit(test_case[2] if test_case else "")
        self.description_edit = QTextEdit(test_case[3] if test_case else "")
        self.steps_edit = QTextEdit(test_case[4] if test_case else "")
        self.expected_result_edit = QTextEdit(test_case[5] if test_case else "")
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Alta", "Media", "Baja"])
        if test_case:
            self.priority_combo.setCurrentText(test_case[6])

        self.layout.addRow("Nombre:", self.name_edit)
        self.layout.addRow("Descripción:", self.description_edit)
        self.layout.addRow("Pasos:", self.steps_edit)
        self.layout.addRow("Resultado Esperado:", self.expected_result_edit)
        self.layout.addRow("Prioridad:", self.priority_combo)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    # Devuelve los datos introducidos en el diálogo.
    def get_data(self):
        return (
            self.name_edit.text(),
            self.description_edit.toPlainText(),
            self.steps_edit.toPlainText(),
            self.expected_result_edit.toPlainText(),
            self.priority_combo.currentText()
        )
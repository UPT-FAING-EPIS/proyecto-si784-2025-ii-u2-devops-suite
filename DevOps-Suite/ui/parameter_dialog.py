from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox

class ParameterDialog(QDialog):
    def __init__(self, parameters):
        super().__init__()
        self.setWindowTitle("Configurar Parámetros")
        self.layout = QFormLayout(self)

        self.parameter_edits = {}
        for param_name in parameters:
            self.parameter_edits[param_name] = QLineEdit()
            self.layout.addRow(param_name, self.parameter_edits[param_name])

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def get_parameters(self):
        return {name: edit.text() for name, edit in self.parameter_edits.items()}

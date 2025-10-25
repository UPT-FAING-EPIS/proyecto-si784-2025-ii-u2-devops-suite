import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QTableWidgetItem, QMessageBox, QFileDialog
import database
from ui import MainUI
from test_case_dialog import TestCaseDialog
from report_generator import export_to_pdf, export_to_excel

class TestCaseManager(QMainWindow):
    # Constructor de la clase de la ventana principal.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Casos de Prueba")
        self.setGeometry(100, 100, 800, 600)

        self.conn = database.create_connection()
        database.create_tables(self.conn)

        self.main_ui = MainUI()
        self.setCentralWidget(self.main_ui)

        self.main_ui.new_project_button.clicked.connect(self.add_project)
        self.main_ui.project_combo.currentIndexChanged.connect(self.load_test_cases)
        self.main_ui.new_test_case_button.clicked.connect(self.add_test_case)
        self.main_ui.execute_test_button.clicked.connect(self.execute_test)
        self.main_ui.report_button.clicked.connect(self.generate_report)
        self.load_projects()

    # Carga los proyectos de la base de datos en el ComboBox.
    def load_projects(self):
        self.main_ui.project_combo.clear()
        projects = database.get_projects(self.conn)
        for project in projects:
            self.main_ui.project_combo.addItem(project[1], project[0])

    # Añade un nuevo proyecto a la base de datos.
    def add_project(self):
        name, ok = QInputDialog.getText(self, "Nuevo Proyecto", "Introduce el nombre del proyecto:")
        if ok and name:
            database.create_project(self.conn, name)
            self.load_projects()

    # Carga los casos de prueba del proyecto seleccionado en la tabla.
    def load_test_cases(self):
        project_id = self.main_ui.project_combo.currentData()
        if project_id:
            test_cases = database.get_test_cases_by_project(self.conn, project_id)
            self.main_ui.test_case_table.setRowCount(len(test_cases))
            for row, test_case in enumerate(test_cases):
                for col, data in enumerate(test_case):
                    self.main_ui.test_case_table.setItem(row, col, QTableWidgetItem(str(data)))

    # Añade un nuevo caso de prueba a la base de datos.
    def add_test_case(self):
        project_id = self.main_ui.project_combo.currentData()
        if project_id:
            dialog = TestCaseDialog()
            if dialog.exec_():
                test_case_data = dialog.get_data()
                database.create_test_case(self.conn, (project_id,) + test_case_data)
                self.load_test_cases()

    # Ejecuta una prueba y actualiza su resultado en la base de datos.
    def execute_test(self):
        selected_row = self.main_ui.test_case_table.currentRow()
        if selected_row >= 0:
            test_case_id = self.main_ui.test_case_table.item(selected_row, 0).text()
            reply = QMessageBox.question(self, 'Ejecutar Prueba', '¿Pasó o Falló?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            result = "Pasa" if reply == QMessageBox.Yes else "Falla"
            database.update_test_case_result(self.conn, test_case_id, result)
            self.load_test_cases()

    # Genera un informe de resumen de las pruebas.
    def generate_report(self):
        project_id = self.main_ui.project_combo.currentData()
        if project_id:
            test_cases = database.get_test_cases_by_project(self.conn, project_id)
            total = len(test_cases)
            if total > 0:
                passed = sum(1 for tc in test_cases if tc[4] == "Pasa")
                failed = sum(1 for tc in test_cases if tc[4] == "Falla")
                pending = total - passed - failed
                success_rate = (passed / total) * 100
                report = f"Total de Casos de Prueba: {total}\nPasaron: {passed}\nFallaron: {failed}\nPendientes: {pending}\nPorcentaje de Éxito: {success_rate:.2f}%"
                reply = QMessageBox.question(self, 'Informe de Pruebas', report + "\n\n¿Exportar informe?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.export_report(test_cases)

    # Exporta el informe a un archivo PDF o Excel.
    def export_report(self, test_cases):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Informe", "", "Archivos PDF (*.pdf);;Archivos de Excel (*.xlsx)", options=options)
        if fileName:
            if fileName.endswith(".pdf"):
                export_to_pdf(test_cases, fileName)
            elif fileName.endswith(".xlsx"):
                export_to_excel(test_cases, fileName)

# Punto de entrada de la aplicación.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TestCaseManager()
    main_window.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QHBoxLayout, QLabel, QInputDialog, QComboBox, QFileDialog
import sys
import os
import inspect

# Añadir el directorio src al sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from automation import scripts
from automation.workflow import Workflow, WorkflowStep
from parameter_dialog import ParameterDialog

class AutomationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Lista de scripts preconfigurados
        self.script_list = QListWidget()
        self.layout.addWidget(self.script_list)

        self.load_scripts()

        self.workflow = Workflow()

        # Área del flujo de trabajo
        self.workflow_area = QListWidget()
        self.layout.addWidget(self.workflow_area)

        # Botones de control
        self.control_buttons = QWidget()
        self.control_layout = QHBoxLayout(self.control_buttons)
        self.add_button = QPushButton("Añadir")
        self.remove_button = QPushButton("Eliminar")
        self.configure_button = QPushButton("Configurar")
        self.run_button = QPushButton("Ejecutar")
        self.control_layout.addWidget(self.add_button)
        self.control_layout.addWidget(self.remove_button)
        self.control_layout.addWidget(self.configure_button)
        self.control_layout.addWidget(self.run_button)
        self.layout.addWidget(self.control_buttons)

        self.add_button.clicked.connect(self.add_step)
        self.remove_button.clicked.connect(self.remove_step)
        self.configure_button.clicked.connect(self.configure_step)
        self.run_button.clicked.connect(self.run_workflow)

    def load_scripts(self):
        script_names = [name for name, func in inspect.getmembers(scripts, inspect.isfunction) if name.startswith('run')]
        self.script_list.addItems(script_names)

    def add_step(self):
        selected_script = self.script_list.currentItem()
        if selected_script:
            step = WorkflowStep(selected_script.text())
            self.workflow.add_step(step)
            self.update_workflow_display()

    def remove_step(self):
        selected_item = self.workflow_area.currentItem()
        if selected_item:
            row = self.workflow_area.row(selected_item)
            self.workflow.remove_step(row)
            self.update_workflow_display()

    def configure_step(self):
        selected_item = self.workflow_area.currentItem()
        if selected_item:
            row = self.workflow_area.row(selected_item)
            step = self.workflow.steps[row]
            if step.script_name == 'run_git_push':
                project_path = QFileDialog.getExistingDirectory(self, 'Select Project Directory')
                if project_path:
                    commit_message, ok = QInputDialog.getText(self, 'Commit Message', 'Enter the commit message:')
                    if ok and commit_message:
                        branch, ok = QInputDialog.getItem(self, 'Branch', 'Select the branch:', ['main', 'master'], 0, False)
                        if ok and branch:
                            step.parameters = {'project_path': project_path, 'commit_message': commit_message, 'branch': branch}
                            self.update_workflow_display()
            elif step.script_name == 'run_git_clone':
                repo_url, ok = QInputDialog.getText(self, 'Repository URL', 'Enter the repository URL:')
                if ok and repo_url:
                    destination = QFileDialog.getExistingDirectory(self, 'Select Destination Directory')
                    if destination:
                        step.parameters = {'repo_url': repo_url, 'destination': destination}
                        self.update_workflow_display()
            else:
                param_names = scripts.get_script_parameters(step.script_name)
                dialog = ParameterDialog(param_names)
                if dialog.exec_():
                    step.parameters = dialog.get_parameters()
                    self.update_workflow_display()

    def run_workflow(self):
        for step in self.workflow.steps:
            scripts.run_script(step.script_name, step.parameters)

    def update_workflow_display(self):
        self.workflow_area.clear()
        for step in self.workflow.steps:
            param_str = ", ".join([f'{k}={v}' for k, v in step.parameters.items()])
            self.workflow_area.addItem(f'{step.script_name}({param_str})')
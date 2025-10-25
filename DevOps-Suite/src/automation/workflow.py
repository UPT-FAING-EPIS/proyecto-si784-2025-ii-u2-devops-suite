class WorkflowStep:
    def __init__(self, script_name, parameters=None):
        self.script_name = script_name
        self.parameters = parameters if parameters else {}

class Workflow:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def remove_step(self, step_index):
        del self.steps[step_index]

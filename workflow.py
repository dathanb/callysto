import yaml

from shell_script import ShellScript
from shell_variable import ShellVariable


class Workflow:
    bindings: dict
    steps: [ShellScript]

    def __init__(self, workflow_definition_file):
        with open(workflow_definition_file, "r") as stream:
            workflow_string = stream.read()
        data = yaml.safe_load(workflow_string)
        print(data)
        self.build_bindings(data)
        self.build_workflow_steps(data)

    def build_bindings(self, data):
        self.bindings = dict()
        if 'bindings' not in data:
            return

        for variable_name in data['bindings']:
            self.bindings[variable_name] = ShellVariable(variable_name, data['bindings'][variable_name])

    def build_workflow_steps(self, data):
        self.steps = []
        for step_data in data['steps']:
            input_variables = []
            if 'input_variables' in step_data:
                input_variables = step_data['input_variables']
            output_variables = []
            if 'output_variables' in step_data:
                output_variables = step_data['output_variables']
            self.steps.append(ShellScript(self.bindings, input_variables, output_variables, step_data['script']))

    def run(self):
        for step in self.steps:
            step.run()


class WorkflowStep:
    """
    A single step in a workflow, including the command / script to run, any dependencies, input and output variables.
    """

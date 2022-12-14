import yaml

from shell_script import ShellScript
from shell_variable import ShellVariable


class Workflow:
    bindings: dict
    steps: [ShellScript]
    state_file: str | None

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as stream:
            workflow_string = stream.read()
        return Workflow(workflow_string)

    def __init__(self, workflow_definition: str):
        data = yaml.safe_load(workflow_definition)
        self.build_bindings(data)
        self.build_workflow_steps(data)
        self.state_file = None

    def with_state_file(self, filename):
        self.state_file = filename

    def build_bindings(self, data):
        self.bindings = dict()
        if 'bindings' not in data:
            return

        for variable_name in data['bindings']:
            self.bindings[variable_name] = ShellVariable(variable_name, data['bindings'][variable_name])

    def build_workflow_steps(self, data):
        self.steps = []
        if 'steps' not in data:
            return
        for step_data in data['steps']:
            if step_data['type'] != 'bash':
                raise NotImplementedError(f"Step type {step_data['type']} is not supported")
            input_variables = []
            if 'input_variables' in step_data:
                input_variables = step_data['input_variables']
            output_variables = []
            if 'output_variables' in step_data:
                output_variables = step_data['output_variables']
            self.steps.append(ShellScript(self.bindings, input_variables, output_variables, step_data['script']))

    def run(self):
        results = dict()
        results['steps'] = []
        for step in self.steps:
            step.run()
            step_result = dict()
            step_result['output'] = step.output
            if step.exit_code == 0:
                step_result['status'] = 'SUCCESS'
            elif step.exit_code == 64:
                step_result['status'] = 'PENDING'
            else:
                step_result['status'] = 'FAILURE'
            results['steps'].append(step_result)
            if step_result['status'] != 'SUCCESS':
                break
        if self.state_file:
            with open(self.state_file, 'w') as output_file:
                yaml.dump(results, output_file)
        return results


class WorkflowStep:
    """
    A single step in a workflow, including the command / script to run, any dependencies, input and output variables.
    """

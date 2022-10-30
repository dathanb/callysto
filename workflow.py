import yaml

from shell_script import ShellScript


class Workflow:

    def __init__(self, workflow_definition_file):
        self.state = dict()
        self.workflow = self.build_workflow(workflow_definition_file)

    def build_workflow(self, workflow_definition_file):
        with open(workflow_definition_file, "r") as stream:
            workflow_string = stream.read()
        data = yaml.safe_load(workflow_string)
        print(data)
        steps = []
        for step_data in data['steps']:
            input_variables = []
            if 'input_variables' in step_data:
                input_variables = step_data['input_variables']
            output_variables = []
            if 'output_variables' in step_data:
                output_variables = step_data['output_variables']
            steps.append(ShellScript(self.state, input_variables, output_variables, step_data['script']))
        return steps

    def run(self):
        for step in self.workflow:
            step.run()


class WorkflowStep:
    """
    A single step in a workflow, including the command / script to run, any dependencies, input and output variables.
    """

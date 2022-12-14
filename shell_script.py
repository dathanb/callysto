#  run bash
import queue
import subprocess
import threading
import uuid
from subprocess import PIPE

from shell_variable import ShellVariable


class ShellScript:
    state: dict[str, ShellVariable]
    input_vars: [str]
    output_vars: [str]
    script: str
    process_handle: subprocess.Popen
    output: str
    section_separator: str
    exit_code: int

    def __init__(self, state: dict, input_vars: [str], output_vars: [str], script: str):
        self.state = state
        self.input_vars = input_vars
        self.output_vars = output_vars
        self.script = script
        self.done = threading.Event()
        self.input = queue.Queue()
        self.output = ""
        self.section_separator = str(uuid.uuid4())

    def run(self):
        self.process_handle = subprocess.Popen("bash", stdin=PIPE, stdout=PIPE, encoding="utf-8")
        (self.raw_output, stderr) = self.process_handle.communicate(input=self.build_script())
        self.output = self.truncate_output()
        self.update_state()
        self.exit_code = self.process_handle.returncode

    def truncate_output(self):
        """The raw output is expected to contain actual shell output, then the section separator, then output
        variable bindings. Developers shouldn't have to worry about the specifics of the protocol Callysto uses for
        bash scripts, so this method strips off the section separator and everything after it."""
        separator_offset = self.raw_output.find(self.section_separator)
        return self.raw_output[:separator_offset]

    def build_script(self):
        input = []
        # TODO: we can probably just construct a single string and write it all at once
        # set up the script to pass back output vars
        input.append("""function linear_workflow_do_cleanup() {""")
        input.append(f"""    echo "{self.section_separator}\"""")
        for output_var in self.output_vars:
            input.append(f"""    echo "{output_var}:$(echo "${{{output_var}}}" | tr -d '\n' | base64)" """);
        input.append("""}""")
        input.append("""trap linear_workflow_do_cleanup EXIT""")

        # pass input vars into the script
        for input_var in self.input_vars:
            var_value = self.state[input_var].encode()
            input.append(f"""{input_var}="$(echo "{var_value}" | base64 -d)\"""")

        input.append(self.script)

        input.append("exit 0")
        return "\n".join(input)

    def update_state(self):
        separator_offset = self.raw_output.find(self.section_separator)
        output_section = self.raw_output[separator_offset + len(self.section_separator) + 1:].strip()
        output_directives = output_section.split("\n")
        for directive in output_directives:
            if len(directive) == 0:
                # TODO: log this
                continue
            (variable_name, value) = directive.split(":")
            if variable_name in self.state:
                self.state[variable_name].update_from(value)
            else:
                self.state[variable_name] = ShellVariable(variable_name, value, is_base64=True)

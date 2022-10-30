import base64

from shell_script import ShellScript


def test_shell_script_can_return_vars():
    state = dict()
    script = ShellScript(state, [], ['name'], "name=dathan")
    script.run()

    assert state['name'] == str(base64.standard_b64encode(bytes('dathan', encoding='utf-8')), encoding='utf-8')


def test_shell_script_can_accept_input_vars():
    state = {'name': str(base64.standard_b64encode(bytes('dathan', encoding='utf-8')), encoding="utf-8")}
    script = ShellScript(state, ['name'], [], "echo ${name}")
    script.run()
    print(script.output)
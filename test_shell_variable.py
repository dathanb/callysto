from shell_variable import ShellVariable


def test_encode_to_base64():
    var = ShellVariable('name', 'dathan')
    assert var.encode() == "ZGF0aGFu"


def test_encode_already_bas64():
    var = ShellVariable('name', 'ZGF0aGFu', is_base64=True)
    assert var.encode() == 'ZGF0aGFu'


def test_update_non_base64_from_base64():
    var = ShellVariable('name', 'dathan')
    var.update_from('YmVubmV0dA==')
    assert var.value == 'bennett'
    assert var.encode() == 'YmVubmV0dA=='


def test_update_base64_from_base64():
    var = ShellVariable('name', 'dathan', is_base64=True)
    var.update_from('YmVubmV0dA==')
    assert var.value == 'YmVubmV0dA=='
    assert var.encode() == 'YmVubmV0dA=='

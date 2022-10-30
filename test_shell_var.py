from shell_var import ShellVar


def test_encode_to_base64():
    var = ShellVar('name', 'dathan')
    assert var.encode() == "ZGF0aGFu"


def test_encode_already_bas64():
    var = ShellVar('name', 'ZGF0aGFu', is_base64=True)
    assert var.encode() == 'ZGF0aGFu'

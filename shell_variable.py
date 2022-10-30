import base64


class ShellVariable:
    """
    Represents a variable in state that gets passed to and from shell scripts.
    As a convenience, the variable can be constructed initially with a utf-8 encoded string.
    """
    def __init__(self, name, value, is_base64=False):
        self.name = name
        self.value = value
        self.is_base64 = is_base64

    def encode(self):
        """
        Encode the variable value for sending to a shell script.
        To dodge escaping, field separator, newline, etc. issues, we always send the value to the script base64-encoded.
        """
        if self.is_base64:
            # the value's already base64-encoded in memory, so pass it through as-is
            return self.value
        else:
            # need to base64-encode it
            return str(base64.b64encode(bytes(self.value,encoding='utf-8')), encoding='utf-8')

    def update_from(self, value: str):
        if self.is_base64:
            self.value = value
        else:
            self.value = str(base64.b64decode(bytes(value, encoding='utf-8')), encoding='utf-')

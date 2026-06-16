


class RuntimeError(Exception):
    def __init__(self, message, token):
        self.message = message
        self.token = token

    def __str__(self):
        return f"Runtime Error: {self.message} at line {self.token.line}"
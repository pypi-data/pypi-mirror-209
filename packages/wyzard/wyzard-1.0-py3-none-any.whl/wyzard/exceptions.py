class WyzardException(Exception):
    def __init__(self, message: str=None):
        if message is None:
            message = 'An error has occurred within Wyzard'
        super().__init__(message)

class LocalModelNotFound(WyzardException):
    def __init__(self):
        super().__init__("Unable to load local model. Is the model already downloaded and you entered the correct model path?")

class PytorchModelNotFound(WyzardException):
    def __init__(self):
        super().__init__("Unable to find pytorch_model.bin. Did you entered the correct model path?")

class PathDoesntExists(WyzardException):
    def __init__(self, message: str = None):
        super().__init__("Path not found/Doesn't exists.")
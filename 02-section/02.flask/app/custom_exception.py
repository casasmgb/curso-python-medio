import traceback

class CustomException(Exception):
    def __init__(self, code, message, identifier=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.identifier = identifier
        self.stack_trace = traceback.format_exc()

    def __str__(self):
        id_info = f" (ID: {self.identifier})" if self.identifier else ""
        return f"[Error {self.code}]{id_info}: {self.message}"
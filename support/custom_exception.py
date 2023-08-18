class VisibleElementNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ClickableElementNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

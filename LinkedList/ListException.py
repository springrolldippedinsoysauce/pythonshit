class Error(Exception):
    pass


class ListError(Error):
    """Exception raised if list is dieded.

    Attributes:
        message --- explanation of the error
    """

    def __init__(self, message):
        self.message = message
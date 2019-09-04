class Error(Exception):
    pass


class StackOverflowError(Error):
    """Exception raised if stack is overfull.

    Attributes:
        message --- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class StackUnderflowError(Error):
    """Exception raised if stack is underfull.

    Attributes:
        message --- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class QueueOverflowError(Error):
    """Exception raised if queue is overfull.

    Attributes:
        message --- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class QueueUnderflowError(Error):
    """Exception raised if queue is underfull.

    Attributes:
        message --- explanation of the error
    """

    def __init__(self, message):
        self.message = message

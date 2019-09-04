class Error(Exception):
    pass


class IllegalArgumentError(Error):
    def __init__(self, message):
        self.message = message


class NoSuchElementError(Error):
    def __init__(self, message):
        self.message = message


class InsertionError(Error):
    def __init__(self, message):
        self.message = message


class StackOverflowError(Error):
    def __init__(self, message):
        self.message = message


class StackUnderflowError(Error):
    def __init__(self, message):
        self.message = message


class QueueOverflowError(Error):
    def __init__(self, message):
        self.message = message


class QueueUnderflowError(Error):
    def __init__(self, message):
        self.message = message


class ListError(Error):
    def __init__(self, message):
        self.message = message

class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None
        self._prev = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_next(self):
        return self._next

    def get_prev(self):
        return self._prev

    def set_next(self, new_next):
        self._next = new_next

    def set_prev(self, new_prev):
        self._prev = new_prev

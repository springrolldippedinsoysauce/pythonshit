from LinkedList import ListNode


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def is_empty(self):
        empty = (self._head is None)
        return empty

    def insert_first(self, value):
        new_nd = ListNode.ListNode(value)
        if self.is_empty() is True:
            self._head = new_nd
            self._tail = new_nd
        else:
            self._head.set_prev(new_nd)
            new_nd.set_next(self._head)
            self._head = new_nd
            self._head.set_prev(None)
        self._count += 1

    def insert_last(self, value):
        new_nd = ListNode.ListNode(value)
        if self.is_empty() is True:
            self._head = new_nd
            self._tail = new_nd
        else:
            self._tail.set_next(new_nd)
            new_nd.set_prev(self._tail)
            self._tail = new_nd
            self._tail.set_next(None)
        self._count += 1

    def remove_first(self):
        if self.is_empty() is True:
            raise ListError("Don't try it")
        elif self._count == 1:
            node_val = self._head.get_value()
            self._head = None
            self._tail = None
            self._count -= 1
        else:
            node_val = self._head.get_value()
            self._head = self._head.get_next()
            self._head.set_prev(None)
            self._count -= 1
        return node_val

    def remove_last(self):
        if self.is_empty() is True:
            raise ListError("Don't try it")
        elif self._count == 1:
            node_val = self._tail.get_value()
            self._head = None
            self._tail = None
            self._count -= 1
        else:
            node_val = self._tail.get_value()
            self._tail = self._tail.get_prev()
            self._tail.set_next(None)
            self._count -= 1
        return node_val


class Error(Exception):
    pass


class ListError(Error):
    def __init__(self, message):
        self._message = message

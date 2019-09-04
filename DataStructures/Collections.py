from Error import Exceptions


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


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def __iter__(self):
        self.current = self._head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            current_val = self.current.get_value()
            self.current = self.current.get_next()
        return current_val

    def get_count(self):
        return self._count

    def is_empty(self):
        empty = (self._head is None)
        return empty

    def insert_first(self, value):
        new_nd = ListNode(value)
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
        new_nd = ListNode(value)
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
            raise Exceptions.ListError("Linked List is empty!")
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
            raise Exceptions.ListError("Linked List is empty!")
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

    def peek_first(self):
        if self.is_empty() is True:
            raise Exceptions.ListError("Linked List is empty!")
        else:
            node_val = self._head.get_value()
        return node_val

    def peek_last(self):
        if self.is_empty() is True:
            raise Exceptions.ListError("Linked List is empty!")
        else:
            node_val = self._tail.get_value()
        return node_val


class Stack:
    def __init__(self):
        self._stack = LinkedList()

    def push(self, value):
        self._stack.insert_last(value)

    def pop(self):
        popped = self._stack.remove_last()
        return popped

    def top(self):
        top_val = self._stack.peek_last()
        return top_val

    def get_count(self):
        return self._stack.get_count()


class Queue:
    def __init__(self):
        self._queue = LinkedList()
        self._count = 0

    def enqueue(self, value):
        self._queue.insert_last(value)

    def dequeue(self):
        first_val = self._queue.remove_first()
        return first_val

    def peek(self):
        peeked = self._queue.peek_first()
        return peeked

    def get_count(self):
        return self._queue.get_count()

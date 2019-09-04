from StacksAndQueues import Exceptions as EXP


class Stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = []
        self._count = 0

    def get_count(self):
        return self._count

    def is_empty(self):
        empty = (self._count == 0)
        return empty

    def is_full(self):
        full = (self._count == self._capacity)
        return full

    def push(self, value):
        if self.is_full() is True:
            raise EXP.StackOverflowError("Stack is full!")
        else:
            self._stack.append(value)
            self._count += 1

    def pop(self):
        top_val = self.top()
        self._count -= 1
        return top_val

    def top(self):
        if self.is_empty() is True:
            raise EXP.StackUnderflowError("Stack is already empty!")
        else:
            top_val = self._stack[self._count - 1]
        return top_val

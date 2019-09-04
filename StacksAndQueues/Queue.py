from StacksAndQueues import Exceptions as EXP


class Queue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = []
        self._count = 0

    def get_count(self):
        return self._count

    def is_empty(self):
        empty = (self._count == 0)
        return empty

    def is_full(self):
        full = (self._count == self._capacity)
        return full

    def enqueue(self, value):
        if self.is_full() is True:
            raise EXP.QueueOverflowError("Queue is full!")
        else:
            self._queue.append(value)
            self._count += 1

    def dequeue(self):
        front_val = self.peek()
        for i in range(1, self._count):
            self._queue[i - 1] = self._queue[i]
        self._count -= 1
        return front_val

    def peek(self):
        if self.is_empty() is True:
            raise EXP.QueueUnderflowError("Queue is already empty!")
        else:
            front_val = self._queue[0]
        return front_val

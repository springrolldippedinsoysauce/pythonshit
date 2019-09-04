from Error import Exceptions


class HeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def get_priority(self):
        return self.priority

    def get_value(self):
        return self.value


class Heap:
    def __init__(self, max_size):
        self.heap = []
        self.capacity = max_size
        self.count = 0

    def add(self, priority, value):
        if self.count >= self.capacity:
            raise Exceptions.IllegalArgumentError("Heap is full!")
        new_entry = HeapEntry(priority, value)
        self.heap.append(new_entry)
        self.count += 1
        self.trickle_up(self.heap, self.count - 1)

    def remove(self):
        if self.count < 1:
            raise Exceptions.IllegalArgumentError("Heap is empty!")
        temp = self.heap[0]
        self.heap[0] = self.heap[self.count-1]
        self.count -= 1
        self.trickle_down(self.heap, 0, self.count)
        return temp.get_value()

    def trickle_up(self, heap_array, current_index):
        parent_idx = int((current_index - 1) / 2)
        if current_index > 0:
            if heap_array[current_index].get_priority() > heap_array[parent_idx].get_priority():
                self.swap(heap_array, parent_idx, current_index)
                self.trickle_up(heap_array, parent_idx)

    def trickle_down(self, heap_array, current_idx, num_items):
        left_child_idx = int(current_idx * 2 + 1)
        right_child_idx = int(left_child_idx + 1)

        if left_child_idx < num_items:
            large_idx = left_child_idx
            if right_child_idx < num_items:
                if heap_array[left_child_idx].get_priority() < heap_array[right_child_idx].get_priority():
                    large_idx = right_child_idx
            if heap_array[large_idx].get_priority() > heap_array[current_idx].get_priority():
                self.swap(heap_array, large_idx, current_idx)
                self.trickle_down(heap_array, large_idx, num_items)

    def heapify(self, array):
        for i in range(int(len(array)/2) - 1, 0, -1):
            self.trickle_down(array, i, len(array))

    def heap_sort(self, array):
        self.heapify(array)
        for i in range(int(len(array) / 2) - 1, 0, -1):
            self.swap(array, 0, i)
            self.trickle_down(array, 0, i)

    @staticmethod
    def swap(heap_array, index_a, index_b):
        temp = heap_array[index_a]
        heap_array[index_a] = heap_array[index_b]
        heap_array[index_b] = temp

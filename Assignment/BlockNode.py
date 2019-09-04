import numpy as np


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value


class Node:
    def __init__(self, parent, max_key_size, max_child_size):
        self.key_size = 0
        self.child_size = 0
        self.parent = parent
        self.nodes = np.empty(max_key_size, dtype=Entry)
        self.childrens = np.empty(max_child_size, dtype=Node)
        self.sort_count = 0

    def key_present(self, key: str) -> bool:
        present = False
        index = 0
        while index < self.key_size and not present:
            if self.nodes[index].key == key:
                present = True
            index += 1
        return present

    def insert_node(self, key, value):
        self.nodes[self.key_size] = Entry(key, value)
        self.key_size += 1
        if self.key_size > 1:
            self.entry_sort()

    def insert_child(self, child):
        child.parent = self
        self.childrens[self.child_size] = child
        self.child_size += 1
        if self.child_size > 1:
            self.children_sort()

    def get_node(self, index):
        return self.nodes[index]

    def get_children(self, index):
        return self.childrens[index]

    def get_key_size(self):
        return self.key_size

    def get_child_size(self):
        return self.child_size

    def children_sort(self):
        j = self.child_size - 1
        temp = self.childrens[j]
        while j > 0 and self.childrens[j - 1].get_node(0).get_key() > temp.get_node(0).get_key():
            self.childrens[j] = self.childrens[j - 1]
            j -= 1
        self.childrens[j] = temp

    def entry_sort(self):
        j = self.key_size - 1
        temp = self.nodes[j]
        while j > 0 and self.nodes[j-1].get_key() > temp.get_key():
            self.nodes[j] = self.nodes[j-1]
            j -= 1
        self.nodes[j] = temp

    def remove_child(self, child):
        exist = False
        for i in range(self.child_size):
            if exist:
                self.childrens[i-1] = self.childrens[i]
            exist = self.childrens[i] == child
        self.child_size -= 1
        self.childrens[self.child_size] = None

    def to_string_rec(self, node, level):
        string = f'Level {level}\n'
        for i in range(node.key_size):
            string += self.nodes[i].get_value().get_stock_details() + "\n"
        for j in range(node.child_size):
            string += self.to_string_rec(node.childrens[j], level + 1)
        return string

from Assignment import BlockNode
from FileIO import StockClass
from Error import Exceptions
import math


class BlockTree:
    def __init__(self, order, filename):
        self.root = None
        self.size = 0
        self.height = 0
        self.min_key_size = order
        self.min_child_size = self.min_key_size + 1
        self.max_key_size = self.min_key_size * 2
        self.max_child_size = self.max_key_size + 1
        with open(filename, 'r') as f:
            lines = f.read().split('\n')
            print(f'Contains {len(lines)} stock information')
        for e in lines:
            data = e.split(',')
            if len(data) == 7:
                print("===============================================================================================")
                print("Stock data: ", data)
                ticker = data[0]
                date = data[1]
                opening = data[2]
                high = data[3]
                low = data[4]
                close = data[5]
                volume = data[6]
                stock = StockClass.StockClass(ticker, date, opening, high, low, close, volume)
                self.insert(ticker, stock)
        f.close()

    def get_size(self):
        return self.size

    def get_height(self):
        return self.height

    def get_ideal_height(self):
        return int(math.log(self.size) / math.log(self.max_child_size))

    def insert(self, key, value):
        if self.root is None:
            print(f'First root created, inserted key: {key} and value: {value}')
            self.root = BlockNode.Node(None, self.max_key_size, self.max_child_size)
            self.root.insert_node(key, value)
            self.size += 1
        elif self.root.get_child_size() == 0:
            if self.root.get_key_size() < self.max_key_size - 1:
                print(f'Root has space, inserted key: {key} and value: {value}')
                self.root.insert_node(key, value)
                self.size += 1
            elif self.root.get_key_size() == self.max_key_size - 1:
                print("\033[1mRoot is full, split!\033[0m")
                self.split(self.root)
                self.height += 1
                self.insert(key, value)
        else:
            try:
                self.insert_rec(self.root, key, value)
            except Exceptions.IllegalArgumentError as e:
                print(e.message)

    def insert_rec(self, current, key, value):
        index = 0
        num_keys = current.get_key_size()
        tie_breaker = False
        if current.key_present(key):
            raise Exceptions.IllegalArgumentError(f'Keys must be unique: {key} already present')
        if current.get_child_size() == 0:  # Base case reached
            if current.get_key_size() < self.max_key_size - 1:
                print(f'Node has space, inserted key: {key} and value: {value}')
                current.insert_node(key, value)
                self.size += 1
            elif current.get_key_size() == self.max_key_size - 1:
                print("\033[1mNode to insert is full, split!\033[0m")
                self.split(current)
                self.insert(key, value)
        else:
            while not tie_breaker:
                compare = current.get_node(index).get_key()
                if index == 0 and key <= compare:
                    print(f'Key {key} is lesser than {compare} at index[{index}]')
                    current = current.get_children(index)
                    self.insert_rec(current, key, value)
                    tie_breaker = True
                elif index == num_keys - 1 and key > compare:
                    print(f'Key {key} is larger than {compare} at index[{index}]')
                    current = current.get_children(index)
                    self.insert_rec(current, key, value)
                    tie_breaker = True
                elif index > 0:
                    previous = current.get_node(index - 1).get_key()
                    following = current.get_node(index).get_key()
                    if previous < key <= following:
                        print(f'Key {key} is in between than {previous} and {following} and inserted in index[{index}]')
                        current = current.get_children(index)
                        self.insert_rec(current, key, value)
                        tie_breaker = True
                index += 1

    def split(self, node_to_split):
        j = 0
        node = node_to_split
        num_keys = node.get_key_size()
        median_idx = int(num_keys / 2)
        median_key = node.get_node(median_idx).get_key()
        median_val = node.get_node(median_idx).get_value()

        left_node = BlockNode.Node(None, self.max_key_size, self.max_child_size)
        for i in range(median_idx):
            left_node.insert_node(node.get_node(i).get_key(), node.get_node(i).get_value())
        if node.get_child_size() > 0:
            while j <= median_idx:
                child = node.get_children(j)
                left_node.insert_child(child)
                j += 1

        right_node = BlockNode.Node(None, self.max_key_size, self.max_child_size)
        for i in range(median_idx + 1, num_keys):
            right_node.insert_node(node.get_node(i).get_key(), node.get_node(i).get_value())
        if node.get_child_size() > 0:
            for j in range(median_idx + 1, node.get_child_size()):
                child = node.get_children(j)
                right_node.insert_child(child)

        if node.parent is None:
            new_root = BlockNode.Node(None, self.max_key_size, self.max_child_size)
            new_root.insert_node(median_key, median_val)
            node.parent = new_root
            self.root = new_root
            node = self.root
            node.insert_child(left_node)
            node.insert_child(right_node)
            self.height += 1
        else:
            parent = node.parent
            parent.insert_node(median_key, median_val)
            parent.remove_child(node)
            parent.insert_child(left_node)
            parent.insert_child(right_node)
            if parent.get_key_size() == self.max_key_size:
                self.split(parent)

    def get_storage(self):
        return self.root.to_string_rec(self.root, 1)

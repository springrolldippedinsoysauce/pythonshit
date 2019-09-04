class TreeNode:
    def __init__(self, key, value):
        if key is None:
            raise NullKeyError("Key cannot be null!")
        self._value = value
        self._key = key
        self._left_child = None
        self._right_child = None

    def get_key(self):
        return self._key

    def get_left(self):
        return self._left_child

    def set_left(self, value):
        self._left_child = value
        return self._left_child

    def get_right(self):
        return self._right_child

    def set_right(self, value):
        self._right_child = value
        return self._right_child

    def get_value(self):
        return self._value


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._count = 0

    def get_count(self):
        return self._count

    def find(self, key):
        return self.find_rec(key, self._root)

    def find_rec(self, key, curr_nd):
        if curr_nd is None:
            raise NoSuchElementError("Key is not found")
        elif key == curr_nd.get_key():
            val = curr_nd.get_value()
        elif key < curr_nd.get_key():
            val = self.find_rec(key, curr_nd.get_left())
        else:
            val = self.find_rec(key, curr_nd.get_right())
        return val

    def insert(self, key, value):
        self._root = self.insert_rec(key, value, self._root)

    def insert_rec(self, key, value, curr_nd):
        update_node = curr_nd
        if curr_nd is None:  # Base case!
            new_nd = TreeNode(key, value)
            update_node = new_nd
            self._count += 1
        elif key == curr_nd.get_key():
            raise InsertionError("Key already exist!")
        elif key < curr_nd.get_key():
            curr_nd.set_left(self.insert_rec(key, value, curr_nd.get_left()))
        else:
            curr_nd.set_right(self.insert_rec(key, value, curr_nd.get_right()))
        return update_node

    def delete(self, key):
        self._root = self.delete_rec(key, self._root)

    def delete_rec(self, key, curr_nd):
        update_node = curr_nd
        if curr_nd is None:
            raise NullKeyError("Nothing to delete!")
        elif key == curr_nd.get_key():  # Base case!
            update_node = self.delete_node(curr_nd)
            self._count -= 1
        elif key < curr_nd.get_key():
            curr_nd.set_left(self.delete_rec(key, curr_nd.get_left()))
        else:
            curr_nd.set_right(self.delete_rec(key, curr_nd.get_right()))
        return update_node

    def delete_node(self, delete):
        if delete.get_left() is None and delete.get_right() is None:
            update_node = None
        elif delete.get_left() is not None and delete.get_right() is None:
            update_node = delete.get_left()
        elif delete.get_left() is None and delete.get_right() is not None:
            update_node = delete.get_right()
        else:
            update_node = self.promote_successor(delete.get_right())
            if update_node != delete.get_right():
                update_node.set_right(delete.get_right())
            update_node.set_left(delete.get_left())
        return update_node

    def promote_successor(self, curr_nd):
        successor = curr_nd
        if curr_nd.get_left() is not None:
            successor = self.promote_successor(curr_nd.get_left())
            if successor == curr_nd.get_left():
                curr_nd.set_left(successor.get_right())
        return successor

    def display(self):
        self.display_rec(self._root)

    def display_rec(self, current):
        if current is not None:
            if current.get_left() is not None:
                self.display_rec(current.get_left())
            print(current.get_key(), " -> ", current.get_value())  # In-order traversal
            if current.get_right() is not None:
                self.display_rec(current.get_right())


class Error(Exception):
    pass


class NullKeyError(Error):
    def __init__(self, message):
        self._message = message


class InsertionError(Error):
    def __init__(self, message):
        self._message = message


class NoSuchElementError(Error):
    def __init__(self, message):
        self._message = message

class HashEntry:
    empty = None
    key = None
    value = None
    used = None

    def __init__(self):
        self.empty = True
        self.used = False
        self.key = ""
        self.value = None


class HashTable:
    def __init__(self, max_size):
        if max_size < 1:
            print("Nah")
        # Returns the next lower prime greater than max size unless capacity is prime
        self.capacity = self.next_prime(max_size)
        self.size = 0
        self.hash_table = []
        for i in range(self.capacity):
            self.hash_table.append(HashEntry())
        self.max_step = 0
        self.set_max_step()

    def set_max_step(self):
        self.max_step = self.next_prime(self.capacity / 2)

    def get_size(self):
        return self.size

    def load_factor(self):
        return float(self.size) / float(self.capacity)

    def resize(self):
        # Increase/decrease capacity in order to make load
        print("Current load factor is ", self.load_factor())
        old_capacity = self.capacity
        self.capacity = self.next_prime(int(float(self.size) / 0.5))
        print("New capacity is ", self.capacity)
        self.set_max_step()  # Calculate new step from new capacity
        self.size = 0
        old_table = self.hash_table
        self.hash_table = []
        for i in range(self.capacity):
            self.hash_table.append(HashEntry)  # New table

        for j in range(old_capacity):
            if old_table[j].empty is False:
                self.put(old_table[j].key, old_table[j].value)
        print("Resize called ==> new capacity: ", self.capacity)

    def next_prime(self, start):
        if start % 2 == 0:  # Even numbers aren't prime
            prime = start + 1
        else:
            prime = start
        is_prime = self.check_prime(prime)  # Check if already prime

        while is_prime is False:
            prime += 2
            is_prime = self.check_prime(prime)
        return prime

    # Generates a unique integer index from passed key
    def hash(self, key):
        hash_idx = hash(key)
        return hash_idx % self.capacity

    # Generates a second index for double hashing
    @staticmethod
    def probe_hash(key):
        hash_idx = hash(key)
        return hash_idx

    # Insert value into hash table

    #  Returns true if passed int is prime
    @staticmethod
    def check_prime(prime):
        i = 3
        is_prime = True
        while i * i <= prime and prime is True:
            if prime % i == 0:
                is_prime = False
            i += 2
        return is_prime

    def put(self, key, value):
        if self.load_factor() >= 0.6:
            self.resize()
        index = self.hash(key)
        step = self.probe_hash(key)
        if self.hash_table[index].empty is True:
            print(f'Inserting {value} with key {key} at index {index}')
            self.hash_table[index].key = key
            self.hash_table[index].value = value
            self.hash_table[index].empty = False
            self.hash_table[index].used = True
            self.size += 1
        else:
            self.insert_linear_probing(index, key, value, step)

    def insert_linear_probing(self, index, key, value, step):
        loop = False
        while loop is False:
            index = (index + step) % self.capacity
            if self.hash_table[index].empty is True:
                loop = True  # Replacement for Do-While
        print(f'Inserting {value} with key {key} at index {index}')
        self.hash_table[index].key = key
        self.hash_table[index].value = value
        self.hash_table[index].empty = False
        self.hash_table[index].used = True
        self.size += 1

    def find(self, key):
        index = self.hash(key)
        step = self.probe_hash(key)
        if self.hash_table[index].key == key:
            value = self.hash_table[index].value
        else:
            value = self.find_linear_probing(index, key, step)
        return value

    def find_linear_probing(self, index, key, step):
        value = None
        loop = False
        while loop is False:
            if self.hash_table[index].used is False:
                raise NoSuchElementError(f'No element with key {key} exists in the table.\n')
            index = (index + step) % self.capacity
            if self.hash_table[index].key == key:
                value = self.hash_table[index].value
                loop = True
        return value

    def remove(self, key):
        if self.load_factor() <= 0.4:
            self.resize()
        index = self.hash(key)
        step = self.probe_hash(key)
        if self.hash_table[index].key == key:
            self.hash_table[index].key = ""
            self.hash_table[index].value = None
            self.hash_table[index].empty = True
            self.size -= 1
        else:
            self.remove_linear_probing(index, key, step)

    def remove_linear_probing(self, index, key, step):
        loop = False
        while loop is False:
            if self.hash_table[index].used is False:
                raise NoSuchElementError(f'No element with key {key} exists in the table.\n')
            index = (index + step) % self.capacity
            if self.hash_table[index].key == key:
                loop = True
        self.hash_table[index].key = ""
        self.hash_table[index].value = None
        self.hash_table[index].empty = True
        self.size -= 1

class Error(Exception):
    pass


class NoSuchElementError(Error):
    """Exception raised if list encounters an error.

    Attributes:
        message --- explanation of the error
    """

    def __init__(self, message):
        self._message = message

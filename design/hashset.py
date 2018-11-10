"""Design a HashSet without using any built-in hash table libraries."""


class MyHashSet:
    def __init__(self):
        self.arr = [False] * 1000000

    def add(self, key):
        self.arr[key] = True

    def remove(self, key):
        self.arr[key] = False

    def contains(self, key):
        return self.arr[key]


"""One with an actual hash function, albeit really simple."""


class MyHashSet:
    def __init__(self):
        self.cap = 10000
        self.size = 0
        self.set = [None] * self.cap

    def hash(self, key):
        return key % self.cap

    def add(self, key):
        if self.contains(key):
            return

        hash_key = self.hash(key)
        if not self.set[hash_key]:
            self.set[hash_key] = []
        self.set[hash_key].append(key)

    def remove(self, key):
        if not self.contains(key):
            return

        hash_key = self.hash(key)
        self.set[hash_key].remove(key)

    def contains(self, key):
        hash_key = self.hash(key)
        if not self.set[hash_key]:
            return False
        for k in self.set[hash_key]:
            if k == key:
                return True
        return False

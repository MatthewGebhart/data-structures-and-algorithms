# Set:

# We are given a key - value pair
# 1. hash the key
# 2. find the corresponding index of the bucket
# 3. add the key - value pair to that bucket

# Get:

# We are given just a key
# 1. hash the key
# 2. find index of bucket
# 3. traverse the bucket and return the value

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        if not self.head:
            return "NULL"
        current = self.head
        string = ""
        while current:
            string += str(current.value) + " -> "
            current = current.next
        string += "NULL"
        return string

    def insert(self, item):
        old = self.head
        self.head = Node(item)
        self.head.next = old


class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self._buckets = [[] for x in range(self.size)]

    # The hashing algorithm
    def hash(self, key):
        """
        Takes in a string called the 'key',
        and returns a integer representing an
        index of _buckets
        """
        return hash(key) % self.size


    def set(self, key, value):
        """
        Given a key - value pair, hash the key,
        and insert the pair into the correct bucket
        """
        index = self.hash(key)
        found = False
        for i, kv in enumerate(self._buckets[index]):
            if kv[0] == key:
                self._buckets[index][i] = (key, value)
                found = True
                break
        if not found:
            self._buckets[index].append((key, value))
    def get(self, key):
        """
        Given a key, return the value. If the key doesn't
        exist raise an error
        """
        index = self.hash(key)
        for kv in self._buckets[index]:
            if kv[0] == key:
                return kv[1]
        return None
    def has(self, key):
        index = self.hash(key)
        for kv in self._buckets[index]:
            if kv[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            for key_value in bucket:
                keys.append(key_value[0])
        return keys


if __name__ == "__main__":
    ht_1 = Hashtable()
    ht_1.set("name", "Matt")
    print(ht_1.get("name"))

    ht_1.set("age", 37)
    print(ht_1.get("age"))

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
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def set(self, key, value):
        """
        Given a key - value pair, hash the key,
        and insert the pair into the correct bucket
        """
        hashed_key = self.hash(key)

        if self._buckets[hashed_key] is None:
            self._buckets[hashed_key] = LinkedList()
            self._buckets[hashed_key].insert([key, value])
        # self._buckets[hashed_key] is a LinkedList
        else:
            self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        """
        Given a key, return the value. If the key doesn't
        exist raise an error
        """
        # index = self.hash(key)
        # for kv in self._buckets[index]:
        #     if kv[0] == key:
        #         return kv[1]
        # return None

        hashed_key = self.hash(key)

        bucket = self._buckets[hashed_key]

        # We have a LinkedList!
        current = bucket.head

        # traverse our linkedlist
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        raise KeyError(f"Key not found: {key}")
    def has(self, key):
       if self.get(key):
           return True
       else:
           return False


    def keys(self):
        keys = []
        for bucket in self._buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    keys.append(current.value[0])
                    current = current.next
        return keys

        # The hashing algorithm
    def hash(self, key):
        """
        Takes in a string called the 'key',
        and returns a integer representing an
        index of _buckets
        """
        hash = 0

        for char in key:
            hash += ord(char)

        # hash represents the index of the bucket in the hashtable
        hash = (hash * 19) % self.size

        return hash


if __name__ == "__main__":
    ht_1 = Hashtable()
    ht_1.set("name", "Matt")
    print(ht_1.get("name"))

    ht_1.set("age", 37)
    print(ht_1.get("age"))

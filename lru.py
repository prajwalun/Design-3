# The LRUCache class implements a Least Recently Used (LRU) cache using a hash map and a doubly linked list.

# Initialization:
# - The cache stores key-node pairs in a dictionary.
# - A doubly linked list (DLL) manages the order of nodes for LRU tracking, with dummy head (left) and tail (right).

# Helper Methods:
# - remove: Removes a node from the DLL.
# - insert: Inserts a node at the end of the DLL (most recently used).

# get:
# - If the key exists, move the node to the end of the DLL and return its value.
# - If not, return -1.

# put:
# - If the key exists, remove it from the cache.
# - Add the new key-value pair and insert it into the DLL.
# - If the cache exceeds capacity, remove the least recently used node (first in DLL) and delete it from the cache.

# TC: O(1) - Hash map for lookups and DLL for updates.
# SC: O(n) - Space for the cache and DLL with n elements.


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
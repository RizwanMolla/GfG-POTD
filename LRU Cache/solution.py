#User function Template for python3

# design the class in the most optimal way

from collections import OrderedDict

class LRUCache:
    
    #Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.cache = OrderedDict()

    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    #Function for storing key-value pair.
    def put(self, key, value):
        #code here
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value

"""
This solution uses an OrderedDict to efficiently implement the LRU cache. The get method retrieves values while moving accessed keys to the end of the dictionary to mark them as recently used. The put method updates existing values, removes the least recently used item when capacity is reached, and inserts new values efficiently.
"""
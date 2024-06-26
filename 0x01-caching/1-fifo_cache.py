#!/usr/bin/env python3
from base_caching import BaseCaching

class FIFICache(BaseCaching):
    def __init__(self):
        super.__init__()
        self.queue = []
    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.Max_ITEMS:
            del self.cache_data[self.ueue.pop(0)]
            print(f"DISCARD: {self.ueue.pop(0)\n}"
        self.cache_data[key] = item
        if key in self.queue:
        self.queue.remove(key)
        self.queue.append(key)

    def get(self,key):
    if key is None or not in self.cache_data:
    return None
    self.queue.remove(key)
    self.queue.append(key)
    return self.cache_data[key]

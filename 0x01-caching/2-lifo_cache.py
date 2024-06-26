#!/usr/bin/env python3
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                latest_key = self.stack.pop()
                del self.cache_data[latest_key]
                print(f"DISCARD: {latest_key}")
            self.cache_data[key] = item
            self.stack.append(key)
        else:
            self.cache_data[key] = item
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            return (self.cache_data.get(key, None))

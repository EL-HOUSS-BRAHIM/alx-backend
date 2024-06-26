#!/usr/bin/env python3
""" LIFO Caching file system """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and is a caching
    system with LIFO eviction policy.
    """

    def __init__(self):
        """ LIFO Caching system """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache
         Args:
            key ([type]): [description]
            item ([type]): [description]"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            """ If the key is not in the cache, add it to the cache
             and append it to the stack """
            if len(self.cache_data) >= self.MAX_ITEMS:
                latest_key = self.stack.pop()
                del self.cache_data[latest_key]
                print(f"DISCARD: {latest_key}")
            self.cache_data[key] = item
            self.stack.append(key)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key ([type]): [description]"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return (self.cache_data.get(key, None))

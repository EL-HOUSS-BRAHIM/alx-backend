#!/usr/bin/env python3
"""
    MRUCache inherits from BaseCaching and is a caching
    system with MRU eviction policy.
    """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and is
    a caching system with MRU eviction policy.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """
        Assign the item value to the dictionary
        self.cache_data for the key key.
        Maintain MRU order by updating the usage order list.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            most_recent_key = self.keys.pop()
            del self.cache_data[most_recent_key]
            print(f"DISCARD: {most_recent_key}")

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None

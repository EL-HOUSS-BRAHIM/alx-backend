#!/usr/bin/env python3
"""
    MRUCache inherits from BaseCaching and is a caching
    system with MRU eviction policy.
    """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and is a caching
    system with MRU eviction policy.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign the item value to the dictionary
        self.cache_data for the key key.
        Maintain MRU order by updating the OrderedDict.
        """
        if key is None or item is None:
            return

        # If key already exists, update the value
        # and mark it as recently used
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        # If the cache exceeds the MAX_ITEMS, remove
        # the most recently used item
        if len(self.cache_data) > self.MAX_ITEMS:
            most_recent_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark as recently used
            return self.cache_data[key]
        return None

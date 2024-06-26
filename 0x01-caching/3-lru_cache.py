#!/usr/bin/env python3
""" LRU Caching file """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU Caching system that inherits from BaseCaching
    and uses OrderedDict to track order of
    insertion and access the cache."""

    def __init__(self):
        """ Initialize the LRU Caching system """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if (len(self.cache_data)) > self.MAX_ITEMS:
            oldest_key, oldest_value = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark as recently used
            return self.cache_data[key]
        return None

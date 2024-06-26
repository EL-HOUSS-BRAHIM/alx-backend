#!/usr/bin/env python3
""" Basic dictionary for caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
    and is a caching system """

    def put(self, key, item):
        """ this function will add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ this function will return the value in
        self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return (None)
        return self.cache_data[key]

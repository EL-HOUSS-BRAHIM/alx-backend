#!/usr/bin/env python3
""" FIFO Caching file """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements a
    caching system with FIFO eviction.
    """

    def __init__(self):
        super().__init__()
        self.queue = []  # Initialize a queue to track insertion order

    def put(self, key, item):
        """
        Assign the item value to the dictionary
        self.cache_data for the key key.
        Implement FIFO eviction if the cache
        exceeds its maximum capacity.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.queue.append(key)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

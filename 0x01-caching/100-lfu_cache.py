#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict

class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and is a caching system with LFU eviction policy.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        Assign the item value to the dictionary self.cache_data for the key key.
        Maintain LFU order by updating the frequency and LRU order.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used item
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                
                # If there's a tie, use LRU policy
                if len(lfu_keys) > 1:
                    lfu_key = next(k for k in self.usage_order if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]
                
                # Remove the least frequently used item
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.usage_order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None


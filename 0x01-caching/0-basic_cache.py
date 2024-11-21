#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Adds an item to the cache
        """

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache
        """

        return self.cache_data.get(key, None)

#!/usr/bin/env python3
"""Least Recently Used caching module."""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache implementation with a limit on stored items."""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache with LRU eviction policy.

        Args:
            key: The key to store the item under.
            item: The item to be stored.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key or None if not found.
        """

        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)

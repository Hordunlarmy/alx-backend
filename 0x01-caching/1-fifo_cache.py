#!/usr/bin/env python3
"""First-In First-Out caching module."""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache implementation with a limit on stored items."""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache with FIFO eviction policy.

        Args:
            key: The key to store the item under.
            item: The item to be stored.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the oldest item in the cache
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key or None if not found.
        """
        return self.cache_data.get(key)

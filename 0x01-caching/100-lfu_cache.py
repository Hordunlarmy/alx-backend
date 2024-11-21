#!/usr/bin/env python3
"""Least Frequently Used caching module."""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache implementation with a limit on stored items."""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = {}

    def __update_frequency(self, key):
        """Updates the frequency count for a given key."""
        self.keys_freq[key] = self.keys_freq.get(key, 0) + 1

    def __get_lfu_key(self):
        """Finds the least frequently used key.

        Returns:
            The key with the lowest frequency or the oldest in case of ties.
        """
        return min(
            self.keys_freq,
            key=lambda k: (
                self.keys_freq[k],
                list(self.cache_data.keys()).index(k),
            ),
        )

    def put(self, key, item):
        """Adds an item to the cache with LFU eviction policy.

        Args:
            key: The key to store the item under.
            item: The item to be stored.
        """
        if key is None or item is None:
            return

        if (
            key not in self.cache_data
            and len(self.cache_data) >= BaseCaching.MAX_ITEMS
        ):
            lfu_key = self.__get_lfu_key()
            del self.cache_data[lfu_key]
            del self.keys_freq[lfu_key]
            print("DISCARD:", lfu_key)

        self.cache_data[key] = item
        self.__update_frequency(key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.__update_frequency(key)
            return self.cache_data[key]

        return None

#!/usr/bin/env python3
"""
BasicCache module
"""


class BaseCaching:
    """
    BaseCaching class
    """

    MAX_ITEMS = 4

    def __init__(self):
        """
        BaseCaching class constructor
        """

        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache
        """

        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")

    def put(self, key, item):
        """
        Add an item in the cache
        """

        raise NotImplementedError(
            "put must be implemented in your cache class"
        )

    def get(self, key):
        """
        Get an item by key
        """

        raise NotImplementedError(
            "get must be implemented in your cache class"
        )

"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

Please read the following carefully. This file is used to implement a Map
class which supports efficient insertions, accesses, and deletions of
elements.

There is an Entry type defined in entry.py which *must* be used in your
map interface. The Entry is a very simple class that stores keys and values.
The special reason we make you use Entry types is because Entry extends the
Hashable class in util.py - by extending Hashable, you must implement
and use the `get_hash()` method inside Entry if you wish to use hashing to
implement your map. We *will* be assuming Entry types are used in your Map
implementation.
Note that if you opt to not use hashing, then you can simply override the
get_hash function to return -1 for example.
"""

from typing import Any
from structures.entry import Entry
from structures.linked_list import DoublyLinkedList, DLLNode

class Map:
    """
    An implementation of the Map ADT.
    The provided methods consume keys and values via the Entry type.
    """

    def __init__(self) -> None:
        """
        Construct the map.
        You are free to make any changes you find suitable in this function
        to initialise your map.
        """
        self._capacity = 10
        self._buckets = [None] * self._capacity
        self._size = 0

    ## CHANGE THIS ONLY FOR TESTING NOW!!!
    def _hash_function(self, key):
        # Simple hash function using Python's built-in hash() and modulo with table size
        return hash(key) % self._capacity

    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. If k already exists
        in your map, you must return the old value associated with k. Return
        None otherwise. (We will not use None as a key or a value in our tests).
        Time complexity for full marks: O(1*)
        """
        index = self._hash_function(entry.get_key())

        if self._buckets[index] is None:
            self._buckets[index] = DoublyLinkedList()
        
        bucket = self._buckets[index]

        current_node = bucket.get_head_node()

        while current_node is not None:
            if current_node.get_data().get_key() == entry.get_key():
                old_value = current_node.get_data().get_value()
                current_node.get_data().update_value(entry.get_value())
                return old_value
            current_node = current_node.get_next()
        
        bucket.insert_to_front(entry)
        self._size += 1
        
        return None

    def insert_kv(self, key: Any, value: Any) -> Any | None:
        """
        A version of insert which takes a key and value explicitly.
        Handy if you wish to provide keys and values directly to the insert
        function. It will return the value returned by insert, so keep this
        in mind. You can modify this if you want, as long as it behaves.
        Time complexity for full marks: O(1*)
        """
        entry = Entry(key, value)
        return self.insert(entry)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        For convenience, you may wish to use this as an alternative
        for insert as well. However, this version does _not_ return
        anything. Can be used like: my_map[some_key] = some_value
        Time complexity for full marks: O(1*)
        """
        index = self._hash_function(key)

        if self._buckets[index] is None:
            self._buckets[index] = DoublyLinkedList()
        
        bucket = self._buckets[index]

        current_node = bucket.get_head_node()

        while current_node is not None:
            
            if current_node.get_data().get_key() == key:
                current_node.get_data().update_value(value)
                break
            
            current_node = current_node.get_next()

    def remove(self, key: Any) -> None:
        """
        Remove the key/value pair corresponding to key k from the
        data structure. Don't return anything.
        Time complexity for full marks: O(1*)
        """

        index = self._hash_function(key)

        if self._buckets[index] is None:
            return 
        
        bucket = self._buckets[index]

        current_node = bucket.get_head_node() #first thing

        while current_node is not None:
            if current_node.get_data().get_key() == key:
                prev_node = current_node.get_prev()
                next_node = current_node.get_next()

                if prev_node is not None:
                    prev_node.set_next(next_node)
                else:
                    bucket.set_head(next_node)

                if next_node is not None:
                    next_node.set_prev(prev_node)
                else:
                    bucket.set_tail(prev_node)
                
                self._size -= 1
                return
            
            current_node = current_node.get_next()
        
        # return              

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        Time complexity for full marks: O(1*)
        """
        index = self._hash_function(key)

        if self._buckets[index] is None:
            self._buckets[index] = DoublyLinkedList()
        
        bucket = self._buckets[index]

        current_node = bucket.get_head_node()

        while current_node is not None:
            if current_node.get_data().get_key() == key:
                return current_node.get_data().get_value()
            current_node = current_node.get_next()
        
        return None

    def __getitem__(self, key: Any) -> Any | None:
        """
        For convenience, you may wish to use this as an alternative
        for find()
        Time complexity for full marks: O(1*)
        """
        return self.find(key)

    def get_size(self) -> int:
        """
        Time complexity for full marks: O(1)
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Time complexity for full marks: O(1)
        """
        return self._size == 0 

    def print_map(self) -> None:
        """
        Prints the map with all key-value pairs in a compact format.
        """
        for i, bucket in enumerate(self._buckets):
            if bucket is not None:
                print(f"Bucket {i}: [", end="")
                current_node = bucket.get_head_node()
                first = True
                while current_node is not None:
                    entry = current_node.get_data()
                    if entry is not None:  # Ensure entry is not None
                        if not first:
                            print(", ", end="")
                        print(f"{entry.get_key()}: {entry.get_value()}", end="")
                        first = False
                    current_node = current_node.get_next()
                print("]")
            else:
                print(f"Bucket {i}: []")

    # def print_map(self) -> None:
    #     """
    #     Prints the map in an array format where each bucket is an array and its contents
    #     are also displayed as arrays of key-value pairs.
    #     """
    #     array_representation = []
        
    #     for bucket in self._buckets:
    #         if bucket is not None:
    #             bucket_contents = []
    #             current_node = bucket.get_head_node()
    #             while current_node is not None:
    #                 entry = current_node.get_data()
    #                 bucket_contents.append([entry.get_key(), entry.get_value()])
    #                 current_node = current_node.get_next()
    #             array_representation.append(bucket_contents)
    #         else:
    #             array_representation.append([])

    #     print(array_representation)



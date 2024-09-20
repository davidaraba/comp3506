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
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList

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
        self._capacity = 8 
        self._size = 0 
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.allocate(self._capacity, DoublyLinkedList())

    def _resize_if_needed(self) -> None:
        load_factor = self._size / self._capacity
        if load_factor > 0.7:
            self._resize()
    
    ## REFERENCE THIS 
    def _resize(self) -> None:
        new_capacity = self._capacity * 2  # Double the capacity
        new_buckets = DynamicArray()
        new_buckets.allocate(new_capacity, DoublyLinkedList())  # Allocate new array with None for lazy initialization

        # Rehash all entries in the old buckets
        for i in range(self._capacity):
            bucket = self._buckets.get_at(i)
            if bucket is not None and bucket.get_size() > 0:
                current_node = bucket.get_head_node()
                while current_node is not None:
                    entry = current_node.get_data()
                    new_index = entry.get_hash() % new_capacity

                    # # Lazy initialization: Create a new bucket (DoublyLinkedList) if it's None
                    # if new_buckets.get_at(new_index) is None:
                    #     new_buckets.set_at(new_index, DoublyLinkedList())

                    # Insert the entry into the appropriate bucket
                    new_bucket = new_buckets.get_at(new_index)  # Get the correct bucket
                    new_bucket.insert_to_back(entry)
                    
                    current_node = current_node.get_next()

        # Update the map's capacity and buckets
        self._capacity = new_capacity
        self._buckets = new_buckets
 
    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. If k already exists
        in your map, you must return the old value associated with k. Return
        None otherwise. (We will not use None as a key or a value in our tests).
        Time complexity for full marks: O(1*)
        """
        hash_value = entry.get_hash() 
        index = hash_value % self._capacity
        
        # if self._buckets.get_at(index) is None:
        #     self._buckets.set_at(index, DoublyLinkedList())

        bucket = self._buckets.get_at(index)
        
        current_entry = bucket.find_and_return_element(entry)

        if current_entry:
            old_value = current_entry.get_value()
            current_entry.update_value(entry.get_value())
            return old_value
        
        bucket.insert_to_back(entry)
        self._size += 1
        self._resize_if_needed()
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
        return self.insert_kv(key, value)

    def remove(self, key: Any) -> None:
        """
        Remove the key/value pair corresponding to key k from the
        data structure. Don't return anything.
        Time complexity for full marks: O(1*)
        """
        hash_value = Entry(key, None).get_hash()
        
        index = hash_value % self._capacity

        if self._buckets.get_at(index) is None:
            return None 
        
        bucket = self._buckets.get_at(index)
        entry = Entry(key, None)
        success = bucket.find_and_remove_element(entry)
        if success:
            self._size -= 1

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        Time complexity for full marks: O(1*)
        """
        hash_value = Entry(key, None).get_hash()
        index = hash_value % self._capacity

        if self._buckets.get_at(index) is None:
            return None
        
        bucket = self._buckets.get_at(index)
        entry = Entry(key, None)

        found_element = bucket.find_and_return_element(entry)
        
        if found_element is None:
            return None
        
        return found_element.get_value()

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
        Prints out all the key-value pairs in the map.
        """
        print("Map contents:")
        for i in range(self._capacity):
            bucket = self._buckets.get_at(i)
            if bucket is not None and bucket.get_size() > 0:
                current_node = bucket.get_head_node()
                while current_node is not None:
                    entry = current_node.get_data()
                    print(f"Key: {entry.get_key()}, Value: {entry.get_value()}")
                    current_node = current_node.get_next()
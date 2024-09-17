"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

import math
from typing import Any
from structures.bit_vector import BitVector
from structures.util import object_to_byte_array


class BloomFilter:
    """
    A BloomFilter uses a BitVector as a container. To insert a given key, we
    hash the key using a series of h unique hash functions to set h bits.
    Looking up a given key follows the same logic, but only checks if all
    bits are set or not.

    Note that a BloomFilter is considered static. It is initialized with the
    number of total keys desired (as a parameter) and will not grow. You
    must decide what this means in terms of allocating your bitvector space
    accordingly.

    You can add functions if you need to.

    *** A NOTE ON KEYS ***
    We will only ever use int or str keys.
    We will not use `None` as a key.
    You might like to look at the `object_to_byte_array` function
    stored in util.py -- This function can be used to convert a string
    or integer key into a byte array, and then you can use the byte array
    to make your own hash function (bytes are just integers in the range
    [0-255] of course).
    """

    def __init__(self, max_keys: int) -> None:
        # You should use max_keys to decide how many bits your bitvector
        # should have, and allocate it accordingly.
        self._data = BitVector()
        self._max_keys = max_keys
        self._fp = 0.01
        self._bits = self._calculate_num_bits(max_keys, self._fp)
        self._num_hash_functions = self._calculate_num_hash_functions(self._bits, self._max_keys)
        # self._fp = self._calculate_false_positive(self._num_hash_functions, self._max_keys, self._bits)
        self._capacity = self._data.allocate(self._bits)
        self._num_inserted_keys = 0
        self._is_empty = True
        
            
    def _calculate_num_hash_functions(self, bits: int, keys: int) -> int:
        num_hashes = (bits / keys) * math.log(2)
        return math.ceil(num_hashes)
    
    def _calculate_num_bits(self, keys, fp) -> int:
        num_bits = (-keys * math.log(fp)) / ((math.log(2)) ** 2)
        return math.ceil(num_bits)
    
    def _calculate_false_positive(self, hashes: int, keys: int, bits: int) -> float:
        fp = (1- math.exp((-hashes * keys) // bits)) ** hashes
        return fp 
    
    def _hash_function(self, key_bytes: bytes, index: int) -> int:
        hash_value = 0

        for bytes in key_bytes:
            hash_value = (hash_value * 31 + bytes + index * 17) % (2**32)
        
        return hash_value
        
    def __str__(self) -> str:
        """
        A helper that allows you to print a BloomFilter type
        via the str() method.
        This is not marked. <<<<
        """
        bits = ''.join(str(self._data.get_at(i)) for i in range(self._bits))
        return f"BloomFilter: {bits}"

    def insert(self, key: Any) -> None:
        """
        Insert a key into the Bloom filter.
        Time complexity for full marks: O(1)
        """
        hash_key = object_to_byte_array(key)

        for i in range(self._num_hash_functions):
           hash_value = self._hash_function(hash_key, i)
           index = hash_value % self._bits
           self._data.set_at(index)
        
        self._is_empty = not self._is_empty
        self._num_inserted_keys += 1

    def contains(self, key: Any) -> bool:
        """
        Returns True if all bits associated with the h unique hash functions
        over k are set. False otherwise.
        Time complexity for full marks: O(1)
        """
        
        hash_key = object_to_byte_array(key)

        for i in range(self._num_hash_functions):
           hash_value = self._hash_function(hash_key, i)
           index = hash_value % self._bits
           if self._data.get_at(index) != 1:
               return False
        
        return True

    def __contains__(self, key: Any) -> bool:
        """
        Same as contains, but lets us do magic like:
        `if key in my_bloom_filter:`
        Time complexity for full marks: O(1)
        """
        return self.contains(key)

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._is_empty

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of bits) that the underlying
        BitVector can currently maintain.
        Time complexity for full marks: O(1)
        """
        return self._data.get_size()
    
    def print_filter(self) -> None:
        """
        A helper function that prints the current state of the BloomFilter's bits
        as an array of 0s and 1s.
        """
        bits = [self._data.get_at(i) for i in range(self._bits)]
        print("BloomFilter Bits:", bits)
    
    def calculate_actual_false_positive_rate(self) -> float:
        """
        Calculate the actual false positive rate based on the number of keys inserted.
        """
        m = self._bits  # Total number of bits in the bit vector
        k = self._num_hash_functions  # Number of hash functions
        n = self._num_inserted_keys  # Number of inserted keys

        # If no keys are inserted, the FPR is 0
        if n == 0:
            return 0.0

        # Using the FPR formula
        actual_fpr = (1 - (1 - 1 / m) ** (k * n)) ** k
        return actual_fpr
    
    def compare_fpr(self) -> None:
        """
        Print a comparison between the target FPR and the actual FPR.
        """
        actual_fpr = self.calculate_actual_false_positive_rate()
        print(f"Target FPR: {self._fp}")
        print(f"Actual FPR: {actual_fpr}")


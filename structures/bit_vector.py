"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()
        self._num_bits = 0 
        self._flip = False
        self._reverse = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        # need to convert each element (64 bits) to decimal form 
        # return str(self._data[x] for x in range(self.get_size() / BitVector.BITS_PER_ELEMENT))
        #if revesed, print other way

    def __resize(self) -> None:
        pass

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self.get_size():
            return 
        
        element_index = index // BitVector.BITS_PER_ELEMENT
        bit_position = index % BitVector.BITS_PER_ELEMENT
        
        return (self._data[element_index] >> bit_position) & 1

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index > self._data.get_size():
            return 
        
        element_index = index // BitVector.BITS_PER_ELEMENT
        bit_position = index % BitVector.BITS_PER_ELEMENT

        if self._flip:
            self._data[element_index] &= ~ (1 << bit_position)
        else:
            self._data[element_index] |= (1 << bit_position)

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index > self._data.get_size():
            return 
        
        element_index = index // BitVector.BITS_PER_ELEMENT
        bit_position = index % BitVector.BITS_PER_ELEMENT

        if self._flip:
            self._data[element_index] |= (1 << bit_position)
        else:
            self._data[element_index] &= ~ (1 << bit_position)

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        pass

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        pass

    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        pass

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        self._flip = not self._flip

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """

        for i in range(self._data):
            if dist > 0:
                self._data[i] << dist
                self._data[i] * 2 ^ dist 
            else:
                self._data[i] >> dist 

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """

        for i in range(self._data[i]):
            if dist > 0:
                pass
            else:
                pass

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._data.get_size() * BitVector.BITS_PER_ELEMENT

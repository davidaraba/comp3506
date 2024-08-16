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
        self._data.append(0)
        self._num_bits = 0 
        self._flip = False
        self._reverse = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        bit_string = ""

        for i in range(self._data.get_size()):
            current_element = self._data[i]

        if self._reverse:
            bit_range = range(self._data.get_size() - 1, BitVector.BITS_PER_ELEMENT)
        else: 
            bit_range = range(BitVector.BITS_PER_ELEMENT - 1, -1, -1)
        
        for bit_position in bit_range:
                bit_value = (current_element >> bit_position) & 1
                bit_value ^= self._flip  # Flip the bit if necessary
                bit_string += str(bit_value)    

        return bit_string

    # def __str__(self) -> str:
    #     """
    #     A helper that allows you to print a BitVector type
    #     via the str() method.
    #     """
    #     bit_string = ""

    #     if self._reverse:
    #         element_range = range(self._data.get_size() - 1, -1, -1)
    #     else:
    #         element_range = range(self._data.get_size())

    #     for i in element_range:
    #         current_element = self._data[i]

    #         if self._reverse:
    #             bit_range = range(0, BitVector.BITS_PER_ELEMENT)
    #         else:
    #             bit_range = range(BitVector.BITS_PER_ELEMENT - 1, -1, -1)

    #         for bit_position in bit_range:
    #             bit_value = (current_element >> bit_position) & 1
    #             bit_value ^= self._flip  # Flip the bit if necessary
    #             bit_string += str(bit_value)

    #     return bit_string

    def __resize(self, index: int) -> None:   
        required_size = (index // BitVector.BITS_PER_ELEMENT) + 1
        while self._data.get_size() < required_size:
            self._data.append(0)

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._data.get_size() * BitVector.BITS_PER_ELEMENT:
            return None
        
        if self._reverse:
            index = self._data.get_size() - index - 1
        
        element_index = index // BitVector.BITS_PER_ELEMENT
        bit_position = index % BitVector.BITS_PER_ELEMENT
        
        bit_value = (self._data[element_index] >> bit_position) & 1

        if self._flip:
            bit_value = 1 - bit_value

        return bit_value

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

        if index < 0 or index >= self._data.get_size() * BitVector.BITS_PER_ELEMENT:
            return None
        
        if self._reverse:
            index = self._data.get_size() - index - 1

        element_index = index // BitVector.BITS_PER_ELEMENT
        bit_position = index % BitVector.BITS_PER_ELEMENT

        if self._flip:
            self._data[element_index] &= ~(1 << bit_position)
        else:
            self._data[element_index] |= (1 << bit_position)

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index > self._data.get_size() * BitVector.BITS_PER_ELEMENT:
            return 
        
        if self._reverse:
            index = self._data.get_size() - index - 1
        
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
            
        if state == 0:
            self.unset_at(index)
        else:
            self.set_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """

        element_index = self._num_bits // BitVector.BITS_PER_ELEMENT
        bit_position = self._num_bits % BitVector.BITS_PER_ELEMENT

        if element_index >= self._data.get_size():
            self.__resize(self._num_bits)
        
        if state != 0:
            self._data[element_index] |= (1 << bit_position)
        
        self._num_bits += 1


    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._num_bits >= self._data.get_size() * BitVector.BITS_PER_ELEMENT:
                self.__resize(self._num_bits)

        carry = 0

        for i in range(self._data.get_size() - 1, -1, -1):
            new_carry = self._data[i] & 1  # capture the last bit as carry
            self._data[i] = (self._data[i] >> 1) | (carry << (BitVector.BITS_PER_ELEMENT - 1))
            carry = new_carry

        # Set the new bit at the start of the vector
        if state != 0:
            self._data[0] |= (1 << (BitVector.BITS_PER_ELEMENT - 1))
        else:
            self._data[0] &= ~(1 << (BitVector.BITS_PER_ELEMENT - 1))

        self._num_bits += 1
            

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

        if dist == 0 :
            return
        
        if dist > 0:
            self.__left_shift(dist)
        else:
            self.__right_shift(dist)

    def __left_shift(self, left_dist: int) -> None:
        full_shifts = left_dist // BitVector.BITS_PER_ELEMENT
        bit_shifts = left_dist % BitVector.BITS_PER_ELEMENT

        for i in range(self._data.get_size() -1, -1, -1):
            if i - full_shifts >= 0:
                self._data[i] = (self._data[i - full_shifts] << bit_shifts) & \
                    ((1 << BitVector.BITS_PER_ELEMENT) - 1) # accessing the block full_shifts before i 

                if i - full_shifts - 1 >= 0 and bit_shifts > 0:
                    carry =  (self._data[i - full_shifts - 1] >> \
                            (BitVector.BITS_PER_ELEMENT - bit_shifts))
                    self._data[i] |= carry
            else:
                self._data[i] = 0
    
    def __right_shift(self, right_dist: int) -> None:
        right_dist = - right_dist
        full_shifts = right_dist // BitVector.BITS_PER_ELEMENT
        bit_shifts = right_dist % BitVector.BITS_PER_ELEMENT

        for i in range(self._data.get_size()):
            if i + full_shifts  < self._data.get_size():
                self._data[i] = (self._data[i + full_shifts] >> bit_shifts) 

                if i + full_shifts + 1 < self._data.get_size() and bit_shifts > 0:
                    carry = (self._data[i + full_shifts + 1] << (BitVector.BITS_PER_ELEMENT - bit_shifts)) \
                        & ((1 << BitVector.BITS_PER_ELEMENT) - 1)
                    self._data[i] |= carry
            else:
                self._data[i] = 0

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._num_bits

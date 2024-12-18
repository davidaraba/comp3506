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
        self._prepend_count = 0

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        bit_string = ""
        for i in range(self._num_bits):
            bit_value = self.get_at(i)
            bit_string += "1" if bit_value else "0"
        return bit_string

    def __resize(self) -> None:
        """
        Resizes the dynamic array by doubling its capacity.
        """
        size = self._data.get_size()
        new_capacity = size * 2
        
        new_data = DynamicArray()
        for _ in range(new_capacity):
            new_data.append(0)
        for i in range(size):
            new_data[i] = self._data[i]
        self._data = new_data

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._num_bits:
            return None

        # Adjust the index for reversed state
        if self._reverse:
            adjusted_index = self._num_bits - index - 1
        else:
            adjusted_index = index
        
        element_index = adjusted_index // self.BITS_PER_ELEMENT
        bit_position = adjusted_index % self.BITS_PER_ELEMENT

        if element_index < 0 or element_index >= self._data.get_size():
            return None  # Defensive check: ensure index is in bounds

        # Extract the bit value
        bit_value = (self._data[element_index] >> bit_position) & 1

        # Flip the bit if necessary
        return bit_value ^ int(self._flip)

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
        
        if index < 0 or index >= self._num_bits:
            return
        
        actual_index = self._num_bits - index - 1 if self._reverse else index
        element_index = actual_index // self.BITS_PER_ELEMENT
        bit_position = actual_index % self.BITS_PER_ELEMENT

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
        
        if index < 0 or index >= self._num_bits:
            return
        
        actual_index = self._num_bits - index - 1 if self._reverse else index
        element_index = actual_index // self.BITS_PER_ELEMENT
        bit_position = actual_index % self.BITS_PER_ELEMENT

        if self._flip:
            self._data[element_index] |= (1 << bit_position)
        else:
            self._data[element_index] &= ~(1 << bit_position)

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
        if self._num_bits == self._data.get_size() * self.BITS_PER_ELEMENT:
            self.__resize()

        element_index = self._num_bits // self.BITS_PER_ELEMENT
        bit_position = self._num_bits % self.BITS_PER_ELEMENT
        
        if self._flip:
            if state == 0:
                self._data[element_index] |= (1 << bit_position)
            else:
                self._data[element_index] &= ~(1 << bit_position)
        else:
            if state != 0:
                self._data[element_index] |= (1 << bit_position)
        
        self._num_bits += 1

    def prepend(self, state: int) -> None:
        """
        Add a bit to the front of the vector.
        Time complexity for full marks: O(1*) amortized
        """
        if self._num_bits == self._data.get_size() * self.BITS_PER_ELEMENT:
            self.__resize()

        self._num_bits += 1

        # Adjust existing bits by one position to make room for the new bit at the front
        if self._reverse:
            self.shift(-1)  # Shift all bits right by one
        else:
            self.shift(1)  # Shift all bits left by one

        # Insert the new bit in the first position
        if self._reverse:
            # In reverse, the first bit is at the end of the current bit vector
            self.set_at(self._num_bits - 1 if not self._flip else 0)
        else:
            self.set_at(0 if not self._flip else self._num_bits - 1)

        # Correct the bit's value
        self[0] = state if not self._flip else (1 - state)

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
        if dist == 0:
            return

        if dist > 0:
            self.__left_shift(dist)
        else:
            self.__right_shift(-dist)  

    def __left_shift(self, left_dist: int) -> None:
        full_shifts = left_dist // BitVector.BITS_PER_ELEMENT
        bit_shifts = left_dist % BitVector.BITS_PER_ELEMENT

        for i in range(self._data.get_size() - 1, -1, -1):
            if i - full_shifts >= 0:
                # Perform the left shift and mask to ensure only 64 bits are considered
                self._data[i] = (self._data[i - full_shifts] << bit_shifts) & \
                                ((1 << BitVector.BITS_PER_ELEMENT) - 1)

                # Handle carry bits from the previous block
                if i - full_shifts - 1 >= 0 and bit_shifts > 0:
                    carry = self._data[i - full_shifts - 1] >> \
                            (BitVector.BITS_PER_ELEMENT - bit_shifts)
                    self._data[i] |= carry
            else:
                self._data[i] = 0

    def __right_shift(self, right_dist: int) -> None:
        full_shifts = right_dist // BitVector.BITS_PER_ELEMENT
        bit_shifts = right_dist % BitVector.BITS_PER_ELEMENT

        for i in range(self._data.get_size()):
            if i + full_shifts < self._data.get_size():
                # Perform the right shift
                self._data[i] = self._data[i + full_shifts] >> bit_shifts

                # Handle carry bits from the next block
                if i + full_shifts + 1 < self._data.get_size() and bit_shifts > 0:
                    carry = (self._data[i + full_shifts + 1] << \
                            (BitVector.BITS_PER_ELEMENT - bit_shifts)) & \
                            ((1 << BitVector.BITS_PER_ELEMENT) - 1)
                    self._data[i] |= carry
            else:
                self._data[i] = 0

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise, perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """

        if dist == 0 or self._num_bits == 0:
            return

        dist = dist % self._num_bits  # Normalise rotation within the total number of bits

        if dist > 0:
            self.__left_rotate(dist)
        else:
            self.__right_rotate(-dist)

    def __left_rotate(self, left_rot: int) -> None:
        total_bits = self._num_bits
        left_rot = left_rot % total_bits

        if left_rot == 0:
            return

        # Combine all bits into a single value for rotation
        combined_bits = 0
        for i in range(self._data.get_size()):
            combined_bits |= self._data[i] << (i * BitVector.BITS_PER_ELEMENT)

        # Perform the rotation
        combined_bits = ((combined_bits << left_rot) | (combined_bits >> \
                        (total_bits - left_rot))) & ((1 << total_bits) - 1)

        # Split the bits back into the DynamicArray
        for i in range(self._data.get_size()):
            self._data[i] = (combined_bits >> (i * BitVector.BITS_PER_ELEMENT)) \
            & ((1 << BitVector.BITS_PER_ELEMENT) - 1)

    def __right_rotate(self, right_rot: int) -> None:
        total_bits = self._num_bits
        right_rot = right_rot % total_bits

        if right_rot == 0:
            return

        # Combine all bits into a single value for rotation
        combined_bits = 0
        for i in range(self._data.get_size()):
            combined_bits |= self._data[i] << (i * BitVector.BITS_PER_ELEMENT)

        # Perform the rotation
        combined_bits = ((combined_bits >> right_rot) | \
            (combined_bits << (total_bits - right_rot))) & ((1 << total_bits) - 1)

        # Split the bits back into the DynamicArray
        for i in range(self._data.get_size()):
            self._data[i] = (combined_bits >> (i * BitVector.BITS_PER_ELEMENT)) \
                & ((1 << BitVector.BITS_PER_ELEMENT) - 1)
            
    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._num_bits
    
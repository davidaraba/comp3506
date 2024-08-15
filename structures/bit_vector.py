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

        bit_list = ""

        for i in range (self._data.get_size()):
            bit_list += self.__dec_to_binary(self._data.get_at(i))
            # bit_list += str(self.get_at(i))
        
        return bit_list
        
    def __dec_to_binary(self, number: int) -> str:
        binary_str = ''
        count = 0

        if number == 0:
             binary_str = "0"
             count = 1
        else:
            while number > 0:
                r = number % 2
                binary_str += str(r)
                count += 1
                number = number // 2
                
      
        reversed_binary_str = ""
        for i in range(count - 1, -1, -1):
            reversed_binary_str += binary_str[i]

        padding_needed = 64 - count
        padded_binary = ""

        for _ in range(padding_needed):
            padded_binary += '0'
    
        return padded_binary + reversed_binary_str

    def __resize(self) -> None:
        new_capacity = self._data.get_size() * 2

        new_bit_vector = DynamicArray()

        for _ in range(new_capacity):
            new_bit_vector.append(0)
        
        for j in range(self._data.get_size()):
            new_bit_vector[j] = self._data[j]
        
        self._data = new_bit_vector

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self.get_size():
            return None
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
        if index < 0 or index >= self.get_size():
            return None
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
        if index < 0 or index > self._num_bits:
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

        if index < 0 or index >= self._num_bits:
            return
        
        element_index = index // BitVector.BITS_PER_ELEMENT
        bit_position = index % BitVector.BITS_PER_ELEMENT
        
        if state == 0:
            self._data[element_index] &= ~ (1 << bit_position)
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
            self.__resize()
        
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

        if dist == 0:
            return None
        
        if dist > 0:
            self.__left_rotate(dist)
        else:
            self.__right_rotate(dist)

    def __left_rotate(self, left_rot: int) -> None:
        left_rot = left_rot % BitVector.BITS_PER_ELEMENT

        carry_over = 0
        
        for i in range(self._data.get_size()):
            current_chunk = self._data[i]

            new_carry_over = current_chunk >> (BitVector.BITS_PER_ELEMENT - left_rot)

            self._data[i] = ((current_chunk << left_rot) & ((1 << BitVector.BITS_PER_ELEMENT) - 1)) | carry_over

            carry_over = new_carry_over

        self._data[0] |= carry_over
    

    # def __right_rotate(self, right_rot: int) -> None:
    #     right_rot = right_rot % BitVector.BITS_PER_ELEMENT

    #     carry_over = 0

    #     for i in range(self._data.get_size() - 1, -1, -1):
    #         current_chunk = self._data[i]
            
    #         new_carry_over = current_chunk & ((1 << right_rot) - 1)

    #         self._data[i] = ((current_chunk >> right_rot) & ((1 << BitVector.BITS_PER_ELEMENT) - 1)) | carry_over

    #         carry_over = new_carry_over

    #     self._data[0] |= carry_over

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._num_bits

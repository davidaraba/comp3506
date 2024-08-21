"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

class DynamicArray:
    def __init__(self) -> None:
        self._size = 0
        self._start = 0
        self._capacity = 1
        self._data = [None] * self._capacity 
        self._reversed = False

    def __str__(self) -> str:
        if self._size == 0:
            return "Array is empty" 
    
        if self._reversed:
            return str([self._data[(self._start + self._size - 1 - x) % self._capacity] for x in range(self._size)])
        else:
            return str([self._data[(self._start + x) % self._capacity] for x in range(self._size)])

    def __resize(self) -> None:
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[(self._start + i) % self._capacity]
        
        self._data = new_data
        self._capacity = new_capacity
        self._start = 0
        
    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._size:
            return None
        
        if self._reversed:
            index = self._size - index - 1
            
        actual_index = (self._start + index) % self._capacity
        return self._data[actual_index]

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index) 

    def set_at(self, index: int, element: Any) -> None:
        """
        Set element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._size:
            return 
        
        if self._reversed:
            index = self._size - index - 1

        actual_index = (self._start + index) % self._capacity
        
        self._data[actual_index] = element
        
    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        self.set_at(index, element)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        if self._size == self._capacity:
            self.__resize()
            
        end_index = (self._start + self._size) % self._capacity
        self._data[end_index] = element
        self._size += 1 

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._size == self._capacity:
            self.__resize()

        self._start = (self._start - 1) % self._capacity
        self._data[self._start] = element
        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._reversed = not self._reversed
            
    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """

        # Find the index of the element to remove
        index = -1
        for i in range(self._size):
            actual_index = self._size - i - 1 if self._reversed else i
            if self.get_at(actual_index) == element:
                index = actual_index
                break

        # If the element was found, remove it
        if index != -1:
            for i in range(index, self._size - 1):
                self._data[(self._start + i) % self._capacity] = self._data[(self._start + i + 1) % self._capacity]
            
            self._size -= 1
            
                        
    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        if self._size == 0 or index < 0 or index >= self._size:
            return None
        
        if self._reversed:
            index = self._size - index - 1
        
        removed_element = self.get_at(index)

        for i in range(index, self._size - 1):
            self._data[(self._start + i) % self._capacity] = self._data[(self._start + i + 1) % self._capacity]

        self._size -= 1
        return removed_element
        

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._size == 0

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        return self._size == self._capacity

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """
        if self._size > 1:
            self.__merge_sort(0, self._size)

    def __merge_sort(self, left: int, right: int) -> None:

        if right - left > 1:
            middle = (left + right) // 2
            self.__merge_sort(left, middle)
            self.__merge_sort(middle, right)
            self.__merge(left, middle, right)

    def __merge(self, left: int, middle: int, right: int) -> None:
        left_length = middle - left
        right_length = right - middle

        left_array = [self._data[(self._start + left + i) % self._capacity] for i in range(left_length)]
        right_array = [self._data[(self._start + middle + j) % self._capacity] for j in range(right_length)]

        l = r = 0 
        a = left 

        while l < left_length and r < right_length:
            if left_array[l] <= right_array[r]:
                self._data[(self._start + a) % self._capacity] = left_array[l]
                l += 1
            else:
                self._data[(self._start + a) % self._capacity] = right_array[r]
                r+= 1
            a += 1

        while l < left_length:
            self._data[(self._start + a) % self._capacity] = left_array[l]
            a += 1
            l += 1

        while r < right_length:
            self._data[(self._start + a) % self._capacity] = right_array[r]
            a += 1
            r += 1 
    
    def _insert_at(self, index: int, element: Any) -> None:
        if index < 0 or index > self._size:
            return 
        
        if self._size == self._capacity:
            self.__resize()
        
        if self._reversed:
            index = self._size - index - 1
        
        actual_index = (self._start + index) % self._capacity
        
        for i in range(self._size, index, -1):
            self._data[(self._start + i) % self._capacity] = self._data[(self._start + i - 1) % self._capacity]
        
        self._data[actual_index] = element
        self._size += 1

"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 1
        self._data = [None] * self._capacity 

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        if self._size == 0:
            return "Array is empty" 
        
        array_str = "["

        for x in range(self._size):
            current_data = self.get_at(x)
            array_str += str(current_data)
            if x < self._size - 1:
                array_str += ", "

        return array_str + "]"
    
    def __resize(self) -> str:
        self._capacity *= 2
        new_array = [None] * self._capacity

        for i in range(self._size):
            new_array[i] = self._data[i]
        
        self._data = new_array 
        
    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._capacity:
            return None
        else: 
            return self._data[index]

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        if index < 0 or index >= self._capacity:
            return None
        else:
            return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= self._capacity:
            return None 
        else:
            self._data[index] = element
        
        

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
            
        self._data[self._size] = element 
        self._size += 1 

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._size == self._capacity:
            self.__resize()
        
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[0] = element
        self._size += 1 

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        pass

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        # if self._size == 0:
        #     return None
        
        # index = -1
        # for i in range(self._size):
        #     if self._data[i] == element:
        #         index = i
        #         break

    

    
                        
    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        pass

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
        pass

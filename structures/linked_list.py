"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec] 
    """

    def __init__(self) -> None:
        self._head = None # Initially no head
        self._tail = None # Initally no tail 
        self._size = 0 # Initially no size
        self._reversed = False # Flag to determine if list reversed 

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """

        if self._size == 0: 
            return "List is empty"
        

        if self._reversed:
            current_data = self._tail
        else:
            current_data = self._head  

        node_string_rep = ""

        while current_data is not None:
            node_string_rep += (str(current_data.get_data()))
            if (self._reversed and current_data.get_prev() is not None) or \
                (not self._reversed and current_data.get_next() is not None):
                    node_string_rep += " <-> "
                
            if self._reversed:
                current_data = current_data.get_prev()
            else:
                current_data = current_data.get_next()
                
        return node_string_rep
  
    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """

        if self._size == 0:
            return None
        
        return self._tail.get_data() if self._reversed else self._head.get_data()
        

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """

        if self._head is None:
            return 
        
        if self._reversed:
            self._tail.set_data(data)
        else:
            self._head.set_data(data)
        

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """

        if self._size == 0:
            return None
        
        return self._head.get_data() if self._reversed else self._tail.get_data()
        

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """

        if self._tail is None:
            return
        
        if self._reversed:
            self._head.set_data(data)
        else:
            self._tail.set_data(data)

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        
        new_head_node = Node(data)

        if self._size == 0:
            self._head = new_head_node
            self._tail = new_head_node
            self._size += 1
            return
        
        if self._reversed:
            intial_head = self._tail
            intial_head.set_next(new_head_node)
            new_head_node.set_prev(intial_head)
            self._tail = new_head_node
        else:
            intial_head = self._head
            intial_head.set_prev(new_head_node)
            new_head_node.set_next(intial_head)
            self._head = new_head_node
    
        self._size += 1
        

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """

        new_tail_node = Node(data)

        if self._size == 0:
            self._head = new_tail_node
            self._tail = new_tail_node
            self._size += 1
            return
    
        if self._reversed:
            intial_tail = self._head
            intial_tail.set_prev(new_tail_node)
            new_tail_node.set_next(intial_tail) 
            self._head = new_tail_node    
        else:
            intial_tail = self._tail 
            intial_tail.set_next(new_tail_node)
            new_tail_node.set_prev(intial_tail)
            self._tail = new_tail_node
        
        self._size += 1 


    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """

        if self._size == 0:
            return None
        
        if self._reversed:
            return self.remove_from_back()

        head_data_to_remove = self._head.get_data()
        new_head = self._head.get_next()

        if new_head is not None:
            new_head.set_prev(None)
        else:
            self._tail = None

        self._head = new_head #set the head to the new head
        self._size -= 1 #if you remove something, list decreases 
        return head_data_to_remove
        

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """

        if self._size == 0:
            return None
        
        if self._reversed:
            return self.remove_from_front()       
        
        tail_data_to_remove = self._tail.get_data()
        new_tail = self._tail.get_prev()

        if new_tail is not None:
            new_tail.set_next(None)
        else:
            self._head = None

        self._tail = new_tail
        self._size -= 1
        return tail_data_to_remove

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        if self._size == 0:
            return False
        
        if self._reversed:
            current_node = self._tail
        else:
            current_node = self._head

        while current_node is not None:
            if current_node.get_data() == elem:
                return True
            current_node = current_node.get_next()

        return False

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """

        if self._reversed:
            current_node = self._tail
        else:
            current_node = self._head

        if self._size == 0 or not self.find_element(elem):
            return False
        
        while current_node is not None:
            if current_node.get_data() == elem:
                if current_node.get_prev() is not None:
                    current_node.get_prev().set_next(current_node.get_next())
                else:
                    self._head = current_node.get_next()
                
                if current_node.get_next() is not None:
                    current_node.get_next().set_prev(current_node.get_prev()) 
                else:
                    self._tail = current_node.get_prev()
                
                self._size -= 1 
                return True
            
            current_node = current_node.get_next()
    
        return False

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """

        self._reversed = not self._reversed


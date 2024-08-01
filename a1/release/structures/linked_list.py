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
    """

    def __init__(self) -> None:
        # You probably need to track some data here...
        pass

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        pass

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        pass

    def get_head(self) -> Node | None:
        """
        Return the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        pass

    def set_head(self, node: Node) -> None:
        """
        Replace the leftmost node in the list.
        Time complexity for full marks: O(1)
        """
        pass

    def get_tail(self) -> Node | None:
        """
        Return the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        pass

    def set_tail(self, node: Node) -> None:
        """
        Replace the rightmost node in the list.
        Time complexity for full marks: O(1)
        """
        pass

    """
    More interesting functionality now.
    """

    def insert_to_front(self, node: Node) -> None:
        """
        Insert a node to the front of the list
        Time complexity for full marks: O(1)
        """
        pass

    def insert_to_back(self, node: Node) -> None:
        """
        Insert a node to the back of the list
        Time complexity for full marks: O(1)
        """
        pass

    def remove_from_front(self) -> Node | None:
        """
        Remove and return the front element
        Time complexity for full marks: O(1)
        """
        pass

    def remove_from_back(self) -> Node | None:
        """
        Remove and return the back element
        Time complexity for full marks: O(1)
        """
        pass

    def find_element(self, elem: Any) -> Any | None:
        """
        Looks at the data inside each node of the list and returns the
        node if it matches the input elem; returns None otherwise
        Time complexity for full marks: O(N)
        """
        pass

    def find_and_remove_element(self, elem: Any) -> Any | None:
        """
        Finds, removes, and returns the first instance of elem
        (based on the node data) or returns None if the element is not found.
        Time complexity for full marks: O(N)
        """
        pass

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        pass

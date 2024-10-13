from typing import Any
from collections.abc import Iterator
from random import randint

class HuffmanNode:
    def __init__(self, left = None, right = None, root = None):
        self._left = None
        self._right = None
        self._root = root
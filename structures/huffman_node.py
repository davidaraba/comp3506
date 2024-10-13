class HuffmanNode:
    def __init__(self, symbol=None, frequency=0):
        self._symbol = symbol
        self._frequency = frequency
        self._left = None
        self._right = None

    def __lt__(self, other):
        # This will help the PriorityQueue to compare two HuffmanNodes by frequency
        return self.frequency < other.frequency

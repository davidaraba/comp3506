"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

MallocLabs K-mer Querying Structure
"""

from typing import Any

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not.
"""
from structures.bit_vector import BitVector
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList, Node


class KmerStore:
    """
    A data structure for maintaining and querying k-mers.
    You may add any additional functions or member variables
    as you see fit.
    At any moment, the structure is maintaining n distinct k-mers.
    """

    def __init__(self, k: int) -> None:
        self._k = k
        self._kmers = DynamicArray()
        self._frequencies = DynamicArray()
        self._prefix_sum = DynamicArray()

    def read(self, infile: str) -> None:
        """
        Given a path to an input file, break the sequences into
        k-mers and load them into your data structure.
        """
        with open(infile, 'r') as file:
            for line in file:
                line = line.strip()
                for i in range(len(line) - self._k + 1):
                    kmer = line[i:i + self._k]
                    self.batch_insert([kmer])

    def batch_insert(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, insert them into the data structure.
        The input kmer list contains m elements.
        The targeted time complexity is: O(m log m) + O(n + m) amortized time.
        """
        # Insert the kmers into a DynamicArray
        kmers_array = DynamicArray()
        for kmer in kmers:
            kmers_array.append(kmer)

        # Sort the kmers using the DynamicArray's sort method
        kmers_array.sort()

        i, j = 0, 0
        n = self._kmers.get_size()

        while i < kmers_array.get_size() and j < n:
            kmer_at_j = self._kmers.get_at(j)
            kmer_at_i = kmers_array.get_at(i)
            
            if kmer_at_i < kmer_at_j:
                self._kmers._insert_at(j, kmer_at_i)
                self._frequencies._insert_at(j, 1)
                i += 1
                n += 1
            elif kmer_at_i == kmer_at_j:
                self._frequencies.set_at(j, self._frequencies.get_at(j) + 1)
                i += 1
            else:
                j += 1

        while i < kmers_array.get_size():
            last_index = n - 1
            kmer_at_last = self._kmers.get_at(last_index) if n > 0 else None
            
            if n > 0 and kmer_at_last == kmers_array.get_at(i):
                self._frequencies.set_at(last_index, self._frequencies.get_at(last_index) + 1)
            else:
                self._kmers.append(kmers_array.get_at(i))
                self._frequencies.append(1)
                n += 1
            i += 1

        self._update_prefix_sum(True)


    def _update_prefix_sum(self, insert: bool, index: int = None) -> None:
        if insert:
            # Recompute the prefix sum after an insertion
            current_sum = 0 
            self._prefix_sum = DynamicArray()  # Reset the prefix sum list
            for i in range(self._frequencies.get_size()):
                current_sum += self._frequencies.get_at(i)
                self._prefix_sum.append(current_sum)
        else:
            # Update prefix sum after a deletion at a given index
            if index is not None:
                self._prefix_sum.remove_at(index)  # Remove the corresponding prefix sum entry

                # Update the remaining prefix sums
                current_sum = self._prefix_sum.get_at(index - 1) if index > 0 else 0
                for i in range(index, self._frequencies.get_size()):
                    current_sum += self._frequencies.get_at(i)
                    self._prefix_sum.set_at(i, current_sum)

    def batch_delete(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """
        # Insert the kmers into a DynamicArray
        kmers_array = DynamicArray()
        for kmer in kmers:
            kmers_array.append(kmer)

        # Sort the kmers using the DynamicArray's sort method
        kmers_array.sort()

        i, j = 0, 0
        n = self._kmers.get_size()

        while i < kmers_array.get_size() and j < n:
            kmer_at_j = self._kmers.get_at(j)  # Store the result in a variable
            if kmers_array.get_at(i) == kmer_at_j:
                self._kmers.remove_at(j)
                self._frequencies.remove_at(j)
                n -= 1
                i += 1  # Move to the next k-mer in the input list
                self._update_prefix_sum(False, j)
            elif kmers_array.get_at(i) < kmer_at_j:
                i += 1
            else:
                j += 1

        # Recompute the prefix sum after deletion
        self._update_prefix_sum(True)

    def freq_geq(self, m: int) -> list[str]:
        """
        Given an integer m, return a list of k-mers that occur
        >= m times in your data structure.
        Time complexity for full marks: O(n)
        """
        result = []

        for i in range(self._kmers.get_size()):
            if self._frequencies.get_at(i) >= m:
                result.append(self._kmers.get_at(i))
        return result

    def count(self, kmer: str) -> int:
        """
        Given a k-mer, return the number of times it appears in
        your data structure.
        Time complexity for full marks: O(log n)
        """
        index = self._binary_search(self._kmers, kmer)
        return self._frequencies.get_at(index) if index != -1 else 0 

    def count_geq(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of k-mers that
        are lexicographically greater or equal.
        Time complexity: O(log n) for finding the position, O(n) for summing the frequencies.
        """
        low, high = 0, self._kmers.get_size() - 1

        while low <= high:
            mid = (low + high) // 2
            
            if self._kmers.get_at(mid) < kmer:
                low = mid + 1
            else:
                high = mid - 1

        if low >= self._kmers.get_size():
            return 0
        
        if low == 0:
            return self._prefix_sum.get_at(self._prefix_sum.get_size() - 1)
        else:
            return self._prefix_sum.get_at(self._prefix_sum.get_size() - 1) - (self._prefix_sum.get_at(low - 1) if low > 0 else 0)
        
    def compatible(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of compatible
        k-mers. You will be using the two suffix characters
        of the input k-mer to compare against the first two
        characters of all other k-mers.
        Time complexity for full marks: O(1) :-)
        """
        pass

    
    def _binary_search(self, array: DynamicArray, target: str):
        low, high = 0, array.get_size() - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if array.get_at(mid) == target:
                result = mid
            
            if array.get_at(mid) < target:
                low = mid + 1
            else:
                high = mid - 1

        return result 
    
    def print_kmers(self):
        print("kmers:", [self._kmers.get_at(i) for i in range(self._kmers.get_size())])
        print("frequency:", [self._frequencies.get_at(i) for i in range(self._frequencies.get_size())])
        print("sum:", [self._prefix_sum.get_at(i) for i in range(self._prefix_sum.get_size())])
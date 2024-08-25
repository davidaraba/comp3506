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
        self._compatibility_array = DynamicArray()
        
        for _ in range(16):
            self._compatibility_array.append(0)

    def _char_to_index(self, char: str) -> int:
        if char == 'A':
            return 0
        elif char == 'C':
            return 1
        elif char == 'G':
            return 2
        else:
            return 3
    
    def _get_index(self, first: str, second: str) -> int:
        return (self._char_to_index(first) << 2) | self._char_to_index(second)
    
    def _get_complement_index(self, first: str, second: str) -> int:
        first_complement = self._complement(first)
        second_complement = self._complement(second)
        return self._get_index(first_complement, second_complement)
    
    def _complement(self, nucleotide: str) -> str:
        if nucleotide == 'A':
            return 'T'
        elif nucleotide == 'T':
            return 'A'
        elif nucleotide == 'C':
            return 'G'
        elif nucleotide == 'G':
            return 'C'

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
        Given a list of m k-mers, insert the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """
        kmers_array = DynamicArray()
        for kmer in kmers:
            kmers_array.append(kmer)

            index = self._get_index(kmer[0], kmer[1])
            self._compatibility_array.set_at(index, self._compatibility_array.get_at(index) + 1)
        
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
            kmer_at_i = kmers_array.get_at(i)
            last_index = n - 1
            kmer_at_last = self._kmers.get_at(last_index) if n > 0 else None
            
            if n > 0 and kmer_at_last == kmer_at_i:
                self._frequencies.set_at(last_index, self._frequencies.get_at(last_index) + 1)
            else:
                self._kmers.append(kmer_at_i)
                self._frequencies.append(1)
                n += 1
            i += 1

    def batch_delete(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """

        kmers_array = DynamicArray()
        for kmer in kmers:
            kmers_array.append(kmer)

        kmers_array.sort()

        i, j = 0, 0
        n = self._kmers.get_size()

        while i < kmers_array.get_size() and j < n:
            kmer_at_j = self._kmers.get_at(j)
            kmer_at_i = kmers_array.get_at(i)
            
            if kmer_at_i == kmer_at_j:
                # Subtract the full frequency from the compatibility array
                index = self._get_index(kmer_at_j[0], kmer_at_j[1])
                frequency = self._frequencies.get_at(j)
                self._compatibility_array.set_at(index, self._compatibility_array.get_at(index) - frequency)
                
                # Remove the k-mer and its frequency
                self._kmers.remove_at(j)
                self._frequencies.remove_at(j)
                n -= 1
                i += 1
            elif kmer_at_i < kmer_at_j:
                i += 1
            else:
                j += 1

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
        index = self._binary_search(kmer)
        if index == -1:
            return 0
        return self._frequencies.get_at(index)

    def count_geq(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of k-mers that
        are lexicographically greater or equal.
        Time complexity for full marks: O(log n)
        """
        size = self._kmers.get_size()
        left, right = 0, size - 1
        count = 0
        
        while left <= right:
            mid = (left + right) // 2
            mid_kmer = self._kmers.get_at(mid)
            
            if mid_kmer >= kmer:
                right = mid - 1
            else:
                left = mid + 1

        # `left` is now the first index where the k-mer is >= to the input k-mer
        for i in range(left, size):
            count += self._frequencies.get_at(i)
            
        return count

    def compatible(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of compatible
        k-mers. You will be using the two suffix characters
        of the input k-mer to compare against the first two
        characters of all other k-mers.
        Time complexity for full marks: O(1) :-)
        """
        
        # Use bit manipulation to get the index for compatibility array lookup
        last_two_nucleotides = kmer[-2:]
        index = self._get_complement_index(last_two_nucleotides[0], last_two_nucleotides[1])
        
        # Directly return the precomputed value from the compatibility array
        return self._compatibility_array.get_at(index)

    def _binary_search(self, kmer: str) -> int:
        """
        Performs binary search to find the index of a k-mer.
        Returns the index if found, otherwise returns -1.
        """
        left, right = 0, self._kmers.get_size() - 1
        while left <= right:
            mid = (left + right) // 2
            mid_kmer = self._kmers.get_at(mid)
            
            if kmer == mid_kmer:
                return mid
            elif kmer < mid_kmer:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def print_kmers(self):
        print("kmers:", [self._kmers.get_at(i) for i in range(self._kmers.get_size())])
        print("frequency:", [self._frequencies.get_at(i) for i in range(self._frequencies.get_size())])
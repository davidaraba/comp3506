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
        self._kmers = []
        self._frequencies = []
        self._total_frequency = 0

    def read(self, infile: str) -> None:
        """
        Given a path to an input file, break the sequences into
        k-mers and load them into your data structure.
        """

        with open(infile, 'r') as file:
            for line in file:
                line = line.strip()
                for i in range(len(line) - self.k + 1):
                    kmer = line[i:i+self.k]
                    self.batch_insert([kmer])

    def batch_insert(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """
        
        kmers.sort()  # Sort the input k-mers
        i, j = 0, 0
        n = len(self._kmers)

        while i < len(kmers) and j < n:
            kmer_at_j = self._kmers[j]  # Access the k-mer directly from the list
            if kmers[i] < kmer_at_j:
                self._kmers.insert(j, kmers[i])
                self._frequencies.insert(j, 1)
                self._total_frequency += 1 
                i += 1
                n += 1  # Array size has increased
            elif kmers[i] == kmer_at_j:
                self._frequencies[j] += 1  # Increment the frequency
                self._total_frequency += 1 
                i += 1  # Move to the next k-mer in the input list
            else:
                j += 1  # Move to the next k-mer in the array

        while i < len(kmers):
            if self._kmers and self._kmers[-1] == kmers[i]:
                self._frequencies[-1] += 1  # Increment frequency of the last k-mer
                self._total_frequency += 1 
            else:
                self._kmers.append(kmers[i])
                self._frequencies.append(1)
                self._total_frequency += 1 
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
        kmers.sort()  # Sort the input kmers
        i, j = 0, 0
        n = len(self._kmers)

        while i < len(kmers) and j < n:
            kmer_at_j = self._kmers[j]  # Store the result in a variable
            if kmers[i] == kmer_at_j:
                frequency_to_remove = self._frequencies[j]
                self._total_frequency -= frequency_to_remove
                self._kmers.pop(j)
                self._frequencies.pop(j)
                n -= 1
                i += 1 #check this 
            elif kmers[i] < kmer_at_j:
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

        for i in range(len(self._kmers)):
            if self._frequencies[i] >= m:
                result.append(self._kmers[i])
        return result

    def count(self, kmer: str) -> int:
        """
        Given a k-mer, return the number of times it appears in
        your data structure.
        Time complexity for full marks: O(log n)
        """
    
        index = self._binary_search(self._kmers, kmer)
        return self._frequencies[index] if index != -1 else 0 

    def count_geq(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of k-mers that
        are lexicographically greater or equal.
        Time complexity for full marks: O(log n)
        """
        pass        

    def compatible(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of compatible
        k-mers. You will be using the two suffix characters
        of the input k-mer to compare against the first two
        characters of all other k-mers.
        Time complexity for full marks: O(1) :-)
        """
        pass

    # Any other functionality you may need

    def _binary_search(self, array: list[str], target: str):
        low, high = 0, len(array) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if array[mid] == target:
                result = mid
            
            if array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result 
        
    def _geq_binary_search(self, array: list[str], freqarray: list[int], kmer: str) -> int:
        low, high = 0, len(self._kmers) - 1
        total_frequency = self._total_frequency
        sum_of_frequencies_lower = 0 

        while low <= high:
            mid = (low + high) // 2
            if array[mid] < kmer:
                sum_of_frequencies_lower += freqarray[mid]
                low = mid + 1
            else:
                high = mid - 1

        return total_frequency - sum_of_frequencies_lower
    
    def print_kmers(self):
        print(self._kmers)
        print(self._frequencies)
        print(self._total_frequency)



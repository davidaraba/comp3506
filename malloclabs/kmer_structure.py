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

    def read(self, infile: str) -> None:
        """
        Given a path to an input file, break the sequences into
        k-mers and load them into your data structure.
        """
        try:
            with open(infile, 'r') as file:
                sequence = []
                for line in file:
                    for char in line:
                        if char != '\n' and char != '\r':
                            sequence.append(char)
                
            sequence_length = len(sequence)
            if sequence_length < self._k:
                print("Sequence is too short to generate any k-mers.")
                return
            
            for i in range(sequence_length - self._k + 1):
                kmer = []  # Create an empty list to build the k-mer
                for j in range(i, i + self._k):
                    kmer.append(sequence[j])  # Add characters to the k-mer list
                
                kmer_str = ""  # Initialize an empty string
                for char in kmer:
                    kmer_str += char  # Manually concatenate characters
                
                self._store_kmer(kmer_str) #implement
        except FileNotFoundError:
            print("Unable to locate file provided")
    
    def _store_kmer(self, kmer: str) -> None:
        for i in range(self._kmers.get_size()):
            if self._kmers.get_at(i) == kmer:
                current_frequency = self._frequencies.get_at(i)
                self._frequencies.set_at(i, current_frequency + 1)
                return
            
        self._kmers.append(kmer)
        self._frequencies.append(1)
        
    def batch_insert(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """
        pass

    def batch_delete(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
 
        """
        pass

    def freq_geq(self, m: int) -> list[str]:
        """
        Given an integer m, return a list of k-mers that occur
        >= m times in your data structure.
        Time complexity for full marks: O(n)
        """
        
        result = []
        size = self._kmers.get_size()
        
        for i in range(size):
            if self._frequencies[i] >= m:
                result.append(self._kmers[i])
        return result 

    def count(self, kmer: str) -> int:
        """
        Given a k-mer, return the number of times it appears in
        your data structure.
        Time complexity for full marks: O(log n)
        """

        # for i, k in enumerate(self._kmers):
            
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

    def print_kmers(self) -> None:
        """
        Print all k-mers and their corresponding frequencies stored in the KmerStore.
        """
        print("Stored k-mers and their frequencies:")
        for i in range(self._kmers.get_size()):
            kmer = self._kmers.get_at(i)
            frequency = self._frequencies.get_at(i)
            print(f"{kmer}: {frequency}")
        # print(self._kmers)
        

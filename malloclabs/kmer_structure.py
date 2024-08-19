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
                for line in file:
                    sequence = ""
                    for char in line:
                        if char != '\n' and char != "\r":
                            sequence += char
                        
                sequence_length = 0
                for _ in sequence:
                    sequence_length += 1
                
                for i in range(sequence_length - self._k + 1):
                    kmer = ""
                    for j in range(self._k):
                        kmer += sequence[i + j]
                    self.__store_kmer(kmer)
        except FileNotFoundError:
            print("Unable to locate file provided")
    
    def __store_kmer(self, kmer: str) -> None:
        for i in range(self._kmers.get_size()):
            if self._kmers.get_at(i) == kmer:
                current_frequency = self._frequencies.get_at(i)
                self._frequencies.set_at(i, current_frequency + 1)
                return
            
        self._kmers.append(kmer)
        self._frequencies.append(1)

    def batch_insert(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, insert the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """

        # print(self._kmers)
        # print(self._frequencies)

        batch_kmers = DynamicArray()
        for kmer in kmers:
            batch_kmers.append(kmer)
        batch_kmers.sort()

        inserted_kmers_array = DynamicArray()
        inserted_kmers_array_frequency = DynamicArray()

        i = j = 0

        while i < self._kmers.get_size() and j < batch_kmers.get_size():
            if self._kmers.get_at(i) < batch_kmers.get_at(j): #if element in self < batch 
                inserted_kmers_array.append(self._kmers.get_at(i))
                inserted_kmers_array_frequency.append(self._frequencies.get_at(i))
                i += 1           
            elif self._kmers.get_at(i) > batch_kmers.get_at(j):
                inserted_kmers_array.append(batch_kmers.get_at(j))
                inserted_kmers_array_frequency.append(1)
                j += 1
            else:
                inserted_kmers_array.append(self._kmers.get_at(i))
                inserted_kmers_array_frequency.append(self._frequencies.get_at(i) + 1)
                i += 1
                j += 1
    
        while i < self._kmers.get_size():
            inserted_kmers_array.append(self._kmers.get_at(i))
            inserted_kmers_array_frequency.append(self._frequencies.get_at(i))
            i += 1
    
        while j < batch_kmers.get_size():
            inserted_kmers_array.append(batch_kmers.get_at(j))
            inserted_kmers_array_frequency.append(1)
            j += 1
    
        self._kmers = inserted_kmers_array
        self._frequencies = inserted_kmers_array_frequency

        # print(self._kmers)
        # print(self._frequencies)

    def batch_delete(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
 
        """
        #edge 1:
            #kmer not already in data, do nothing 
        
        #edge 2
            #0 after delete 



        for kmer in kmers:
            if kmer == self._kmers:
                pass



    def freq_geq(self, m: int) -> list[str]:
        """
        Given an integer m, return a list of k-mers that occur
        >= m times in your data structure.
        Time complexity for full marks: O(n)
        """
        
        result = DynamicArray()
        for i in range(self._kmers.get_size()):
            kmer = self._kmers[i]
            frequency = self._frequencies[i]
            if frequency >= m:
                result.append(kmer)
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
        

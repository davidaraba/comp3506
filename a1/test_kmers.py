"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

NOTE: This file is not used for assessment. It is just a driver program for
you to write your own test cases and execute them against your data structures.
"""

# Import helper libraries
import random
import sys
import time
import argparse
import cProfile

from malloclabs.kmer_structure import KmerStore
  

# def test_kmer_store_build(filepath : str):
#     """
#     A set of tests for building a kmer store
#     This is not marked and is just here for you to test your code.
#     """

#     # Initialize KmerStore with k = 3 (example: 3-mers)
#     ks = KmerStore(3)

#     # Create a small test file manually (or assume it exists)
#     test_file = "test_kmers.txt"
    
#     # Write the test DNA sequences to the file
#     with open(test_file, "w") as f:
#         f.write("ACGTACGTAC\n")  # This should produce k-mers of length 3: "ACG", "CGT", "GTA", "TAC", "CGT", "GTA", "TAC"
#         f.write("TACGTACGTA\n")  # Repeated k-mers with overlapping ones

#     # Read the test file into the KmerStore
#     ks.read(test_file)

#     # Manually verify that the k-mers and frequencies are as expected
#     expected_kmers = ["ACG", "CGT", "GTA", "TAC"]
#     expected_frequencies = [2, 2, 2, 2]  # Each should appear twice due to overlapping and repetition

#     # Verify the results
#     for i in range(len(expected_kmers)):
#         kmer = expected_kmers[i]
#         expected_freq = expected_frequencies[i]

#         # Simulate what a 'count' function would return by manually checking the index
#         index = -1
#         for j in range(ks._kmers.get_size()):
#             if ks._kmers.get_at(j) == kmer:
#                 index = j
#                 break
        
#         # If the kmer is found, check the frequency
#         if index != -1:
#             actual_freq = ks._frequencies.get_at(index)
#             assert actual_freq == expected_freq, f"Error: k-mer '{kmer}' expected frequency {expected_freq}, but got {actual_freq}"
#         else:
#             assert False, f"Error: k-mer '{kmer}' not found in KmerStore."
    
#     ks.print_kmers()

#     print("Test passed: All k-mers and their frequencies are correct.")

# def test_kmer_store_build(filepath: str):
#     def profile_test():
#         ks = KmerStore(3)
#         # for i in range(10000):
#         ks.batch_insert(['AAA', 'BBB', 'AAA', 'CCC', 'EEE', 'AAA', 'BBB'])
#         ks.print_kmers()
#         print(ks.freq_geq(2))
#         # x = ks.count_geq('AAA')
#         # print(x)

#     # Run the profiler using runctx
#     cProfile.runctx('profile_test()', globals(), locals())

def test_kmer_store_build(filepath: str):
        # Create a KmerStore with k = 3 (or any k you need)
        store = KmerStore(k=3)

        # Insert some k-mers
        kmers_to_insert = ["ATG", "CGA", "GCT", "TGC", "ATT", "CTC", "CTC", "CTC", "CTC", "ACA", "ACA", "ACA"]
        store.batch_insert(kmers_to_insert)
        store.print_kmers()

        # print(store.freq_geq(2))
        
        # Check compatibility
        print("Testing compatibility...")
        
        kmer_to_test = "CGA"  # Last two characters are "GA", complement is "CT"
        compatible_count = store.compatible(kmer_to_test)
        

        
        # We expect "CCT" and "GCT" to be compatible with "TGA"
        print(f"Number of k-mers compatible with {kmer_to_test}: {compatible_count}")
        # store.batch_delete(["CTC"])
        # compatible_count = store.compatible(kmer_to_test)
        

        
        # # We expect "CCT" and "GCT" to be compatible with "TGA"
        # print(f"Number of k-mers compatible with {kmer_to_test}: {compatible_count}")
        
        # assert compatible_count == 2, f"Expected 2, but got {compatible_count}"

        # # Insert another k-mer that should increase compatibility count
        # store.batch_insert(["CTG"])
        # compatible_count = store.compatible(kmer_to_test)
        
        # # Now "CCT", "GCT", and "CTG" should be compatible
        # print(f"Number of k-mers compatible with {kmer_to_test} after inserting 'CTG': {compatible_count}")
        
        # assert compatible_count == 3, f"Expected 3, but got {compatible_count}"

        # # Test another k-mer
        # kmer_to_test = "TTC"  # Last two characters are "TC", complement is "AG"
        # compatible_count = store.compatible(kmer_to_test)
        
        # # If there's no "AG", compatible_count should be 0
        # print(f"Number of k-mers compatible with {kmer_to_test}: {compatible_count}")
        
        # assert compatible_count == 0, f"Expected 0, but got {compatible_count}"

        # print("All tests passed.")

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing K-mer structure")
    parser.add_argument("--build", type=str, help="Path to a file containing DNA sequences.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.build:
        test_kmer_store_build(args.build)

  
    # You probably want to expand with more testing!

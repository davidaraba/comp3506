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
import pstats
import io

from warmup.warmup import * 

def test_main_character():
    """
    A simple set of tests for the main character problem.
    This is not marked and is just here for you to test your code.
    """
    # Test case 1: No repeats
    assert main_character([1, 2, 3, 4, 5]) == -1, "Test case 1 failed"
    
    # Test case 2: Repeated integer at index 2
    assert main_character([1, 2, 1, 4, 4, 4]) == 2, "Test case 2 failed"
    
    # Test case 3: Repeated integer at index 3
    assert main_character([7, 1, 2, 7]) == 3, "Test case 3 failed"
    
    # Test case 4: No repeats with larger numbers
    assert main_character([60000, 120000, 654321, 999, 1337, 133731337]) == -1, "Test case 4 failed"
    
    # Test case 5: Repeated integers at the start
    assert main_character([123456789, 123456789, 987654321]) == 1, "Test case 5 failed"
    
    # Test case 6: Repeated integers at the end
    assert main_character([1, 2, 3, 4, 5, 5]) == 5, "Test case 6 failed"
    
    # Test case 7: Large input with no repeats (limit test for "It works" scenario)
    large_input_no_repeats = list(range(10000))
    assert main_character(large_input_no_repeats) == -1, "Test case 7 failed"
    
    # Test case 8: Large input with repeats at the end (limit test for "It works" scenario)
    large_input_with_repeats = list(range(9999)) + [5000]
    assert main_character(large_input_with_repeats) == 9999, "Test case 8 failed"
    
    # Test case 9: Exhaustive scenario with 300,000 elements and a repeat
    exhaustive_input = list(range(300000))
    exhaustive_input[299999] = exhaustive_input[0]  # Repeat at the last index
    assert main_character(exhaustive_input) == 299999, "Test case 9 failed"

    # Test case 10: Welcome to COMP3506 scenario with 5,000,000 elements and no repeats
    large_input_no_repeats = list(range(5000000))
    assert main_character(large_input_no_repeats) == -1, "Test case 10 failed"

    # x = main_character(large_input_no_repeats)
    # print(x)
    
    print("All test cases passed!")


def test_missing_odds():
    """
    A simple set of tests for the missing odds problem.
    This is not marked and is just here for you to test your code.
    """

    # comp3506_inputs = random.sample(range(10**16), 5000000)
    # result_comp3506 = missing_odds(comp3506_inputs)
    # print(f"COMP3506 Test Result: {result_comp3506}")
    
   
    # assert missing_odds([1, 2]) == 0
    # assert missing_odds([1, 3]) == 0
    # assert missing_odds([1, 4]) == 3
    # assert missing_odds([4, 1]) == 3
    # assert missing_odds([4, 1, 8, 5]) == 10    # 3 and 7 are missing
    # assert missing_odds([6,7,13,15]) == 20
    assert missing_odds([6,7,13,14]) == 20
    assert missing_odds([5,7,13,15]) == 20
    assert missing_odds([5,7,13,16]) == 20

   
def test_k_cool():
    """
    A simple set of tests for the k cool problem.
    This is not marked and is just here for you to test your code.
    """
    assert k_cool(2, 1) == 1                     # The first 2-cool number is 2^0 = 1
    assert k_cool(2, 3) == 3                    # The third 2-cool number is 2^1 + 2^0 = 3
    assert k_cool(3, 5) == 10                    # The fifth 3-cool number is 3^2 + 3^0 = 10
    assert k_cool(10, 42) == 101010
    assert k_cool(128, 5000) == 9826529652304384 # The actual result is larger than 10^16 + 61,

# def test_number_game():
#     """
#     A simple set of tests for the number game problem.
#     This is not marked and is just here for you to test your code.
#     """

#     assert number_game([5, 2, 7, 3]) == ("Bob", 5)
#     assert number_game([3, 2, 1, 0]) == ("Tie", 0)
#     assert number_game([2, 2, 2, 2]) == ("Alice", 4)
#     assert number_game([1]) == ("Tie", 0)

def profile_number_game():
    pr = cProfile.Profile()
    pr.enable()
    
    # Run your test cases here
    assert number_game([5, 2, 7, 3]) == ("Bob", 5)
    assert number_game([3, 2, 1, 0]) == ("Tie", 0)
    assert number_game([2, 2, 2, 2]) == ("Alice", 4)
    assert number_game([1]) == ("Tie", 0)
    
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

def test_road_illumination():
    """
    A simple set of tests for the road illumination problem.
    This is not marked and is just here for you to test your code.
    """

    x = road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) 
    print(x)

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Warmup Problems")

    parser.add_argument("--character", action="store_true", help="Test your main character sol.")
    parser.add_argument("--odds", action="store_true", help="Test your missing odds sol.")
    parser.add_argument("--kcool", action="store_true", help="Test your k-cool sol.")
    parser.add_argument("--numbergame", action="store_true", help="Test your number game sol.")
    parser.add_argument("--road", action="store_true", help="Test your road illumination sol.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.character:
        test_main_character()

    if args.odds:
        test_missing_odds()

    if args.kcool:
        test_k_cool()

    if args.numbergame:
        profile_number_game()
        # test_number_game()

    if args.road:
        test_road_illumination()


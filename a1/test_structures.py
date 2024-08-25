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

# Import our data structures
from structures.linked_list import Node, DoublyLinkedList
from structures.dynamic_array import DynamicArray 
from structures.bit_vector import BitVector

def test_linked_list():
    """
    A simple set of tests for the linked list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Linked List Tests ====")

    # Consider expanding these tests into your own methods instead of
    # just doing a bunch of stuff here - this is just to get you started
    
    # OK, let's add some strings to a list
    my_list = DoublyLinkedList()
    assert(my_list.get_size() == 0)

    my_list.insert_to_front(Node("hello"))
    my_list.insert_to_back(Node("algorithms"))

    # Have a look - we can do this due to overriding __str__ in the class
    print(str(my_list))
    
    # Now lets try to find a node
    elem = my_list.find_element("algorithms")
    if elem is not None:
        print ("Found node with data = ", elem.get_data())

    # And try to delete one
    elem = my_list.find_and_remove_element("1337")
    if elem is not None:
        print ("Deleted ", elem.get_data())
    else:
        print ("Didn't find element = 1337")

    # And try to delete another one
    elem = my_list.find_and_remove_element("hello")
    if elem is not None:
        print ("Deleted ", elem.get_data())
    else:
        print ("Didn't find element = world")

    # Have another look
    print(str(my_list))

    # OK, now check size
    assert(my_list.get_size() == 1)
    
def test_dynamic_array():
    """
    A simple set of tests for the dynamic array implementation.
    This is not marked and is just here for you to test your code.
    """
    print("==== Executing Dynamic Array Tests ====")
    # Test 1: Basic Operations Without Reversing
    arr = DynamicArray()
    # arr.append(1)
    # arr.append(2)
    # arr.append(3)

    # print("Test 1: Basic Operations Without Reversing")
    # print(f"Array: {arr} | Expected: [1, 2, 3]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 1")
    # print(f"get_at(1): {arr.get_at(1)} | Expected: 2")
    # print(f"get_at(2): {arr.get_at(2)} | Expected: 3")
    # print()

    # # Test 2: Reversing After Basic Operations
    # arr.reverse()

    # print("Test 2: Reversing After Basic Operations")
    # print(f"Array after reverse: {arr} | Expected: [3, 2, 1]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 3")
    # print(f"get_at(1): {arr.get_at(1)} | Expected: 2")
    # print(f"get_at(2): {arr.get_at(2)} | Expected: 1")
    # print()

    # # Test 3: Prepend and Reverse Operations
    # arr = DynamicArray()
    # arr.prepend(3)
    # arr.prepend(2)
    # arr.prepend(1)

    # print("Test 3: Prepend and Reverse Operations")
    # print(f"Array after prepends: {arr} | Expected: [1, 2, 3]")
    # arr.reverse()
    # print(f"Array after reverse: {arr} | Expected: [3, 2, 1]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 3")
    # print(f"get_at(1): {arr.get_at(1)} | Expected: 2")
    # print(f"get_at(2): {arr.get_at(2)} | Expected: 1")
    # print()

    # # Test 4: Reverse Twice (Should return to original order)
    # arr.reverse()  # Reversing again
    # print("Test 4: Reverse Twice (Should return to original order)")
    # print(f"Array after second reverse: {arr} | Expected: [1, 2, 3]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 1")
    # print(f"get_at(1): {arr.get_at(1)} | Expected: 2")
    # print(f"get_at(2): {arr.get_at(2)} | Expected: 3")
    # print()

    # # Test 5: Append After Reverse
    # arr.reverse()
    # arr.append(4)
    # print("Test 5: Append After Reverse")
    # print(f"Array after append: {arr} | Expected: [3, 2, 1, 4]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 3")
    # print(f"get_at(3): {arr.get_at(3)} | Expected: 4")
    # print()

    # # Test 6: Prepend After Reverse
    # arr.prepend(0)
    # print("Test 6: Prepend After Reverse")
    # print(f"Array after prepend: {arr} | Expected: [0, 3, 2, 1, 4]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 0")
    # print(f"get_at(4): {arr.get_at(4)} | Expected: 4")
    # print()

    # # Test 7: Removing Elements Without Reverse
    # arr = DynamicArray()
    # arr.append(1)
    # arr.append(2)
    # arr.append(3)
    # arr.remove(2)

    # print("Test 7: Removing Elements Without Reverse")
    # print(f"Array after removal: {arr} | Expected: [1, 3]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 1")
    # print(f"get_at(1): {arr.get_at(1)} | Expected: 3")
    # print()

    # # Test 8: Removing Elements After Reverse
    # arr.reverse()
    # arr.remove(3)

    # print("Test 8: Removing Elements After Reverse")
    # print(f"Array after reverse and removal: {arr} | Expected: [1]")
    # print(f"get_at(0): {arr.get_at(0)} | Expected: 1")
    # print()

    # # Test 9: Remove at Index Without Reverse
    # arr = DynamicArray()
    # arr.append(1)
    # arr.append(2)
    # arr.append(3)
    # removed_element = arr.remove_at(1)

    # print("Test 9: Remove at Index Without Reverse")
    # print(f"Removed element: {removed_element} | Expected: 2")
    # print(f"Array after removal: {arr} | Expected: [1, 3]")
    # print()

    # # Test 10: Remove at Index After Reverse
    # arr.reverse()
    # removed_element = arr.remove_at(1)

    # print("Test 10: Remove at Index After Reverse")
    # print(f"Removed element: {removed_element} | Expected: 1")
    # print(f"Array after reverse and removal: {arr} | Expected: [3]")
    # print()
    arr.append(1)
    arr.append(3)
    arr.append(9)
    arr.append(4)
    arr.append(60)
    arr.append(86)
    arr.append(1002)
    arr.append(-6)
    arr.append(6)
    arr.append(2193)
    print(arr)

    arr.sort()
    print(arr)
    

    print("==== All Tests Passed! ====")

# def test_bitvector():
#     """
#     A test function to debug BitVector implementation.
#     """
#     print("==== Executing BitVector Tests ====")
#     # Test 1: Basic Operations Without Reversing
#     bv = BitVector()
#     bv.append(1)
#     bv.append(0)
#     bv.append(1)

#     print("Test 1: Basic Operations Without Reversing")
#     print(f"BitVector: {bv} | Expected: 101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 0")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 1")
#     print()

#     # Test 2: Reversing After Basic Operations
#     bv.reverse()

#     print("Test 2: Reversing After Basic Operations")
#     print(f"BitVector after reverse: {bv} | Expected: 101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 0")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 1")
#     print()

#     # Test 3: Prepend and Reverse Operations
#     bv = BitVector()
#     bv.prepend(1)
#     bv.prepend(0)
#     bv.prepend(1)

#     print("Test 3: Prepend and Reverse Operations")
#     print(f"BitVector after prepends: {bv} | Expected: 101")
#     bv.reverse()
#     print(f"BitVector after reverse: {bv} | Expected: 101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 0")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 1")
#     print()

#     # Test 4: Reverse Twice (Should return to original order)
#     bv.reverse()  # Reversing again

#     print("Test 4: Reverse Twice (Should return to original order)")
#     print(f"BitVector after second reverse: {bv} | Expected: 101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 0")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 1")
#     print()

#     # Test 5: Append After Reverse
#     bv.reverse()
#     bv.append(0)

#     print("Test 5: Append After Reverse")
#     print(f"BitVector after append: {bv} | Expected: 1010")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(3): {bv.get_at(3)} | Expected: 0")
#     print()

#     # Test 6: Prepend After Reverse
#     bv.prepend(1)

#     print("Test 6: Prepend After Reverse")
#     print(f"BitVector after prepend: {bv} | Expected: 11010")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(4): {bv.get_at(4)} | Expected: 0")
#     print()

#     # Test 7: Flipping All Bits
#     bv.flip_all_bits()

#     print("Test 7: Flipping All Bits")
#     print(f"BitVector after flipping: {bv} | Expected: 00101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 0")
#     print(f"get_at(4): {bv.get_at(4)} | Expected: 1")
#     print()

#     # Test 8: Prepend After Flipping Bits
#     bv.prepend(1)

#     print("Test 8: Prepend After Flipping Bits")
#     print(f"BitVector after prepend: {bv} | Expected: 100101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(5): {bv.get_at(5)} | Expected: 1")
#     print()

#     # Test 9: Removing Bits Without Reverse
#     bv = BitVector()
#     bv.append(1)
#     bv.append(0)
#     bv.append(1)
#     bv.unset_at(1)

#     print("Test 9: Removing Bits Without Reverse")
#     print(f"BitVector after unset_at(1): {bv} | Expected: 101")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 0")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 1")
#     print()

#     # Test 10: Removing Bits After Reverse
#     bv.reverse()
#     bv.unset_at(1)

#     print("Test 10: Removing Bits After Reverse")
#     print(f"BitVector after reverse and unset_at(1): {bv} | Expected: 100")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 1")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 0")
#     print()

#     # Test 11: Shift Left
#     bv = BitVector()
#     bv.append(1)
#     bv.append(0)
#     bv.append(1)
#     bv.shift(1)

#     print("Test 11: Shift Left")
#     print(f"BitVector after left shift: {bv} | Expected: 010")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 0")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 1")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 0")
#     print()

#     # Test 12: Shift Right
#     bv.shift(-2)

#     print("Test 12: Shift Right")
#     print(f"BitVector after right shift: {bv} | Expected: 001")
#     print(f"get_at(0): {bv.get_at(0)} | Expected: 0")
#     print(f"get_at(1): {bv.get_at(1)} | Expected: 0")
#     print(f"get_at(2): {bv.get_at(2)} | Expected: 1")
#     print()

# def test_bitvector():
#     # Test 1: Simple append and prepend operations
#     bv = BitVector()
#     bv.append(1)
#     bv.append(0)
#     bv.prepend(0)
#     bv.prepend(8)  # 8 should be treated as 1
#     expected = "1001"
#     received = str(bv)
#     print(f"Test 1 - Expected: {expected}, Received: {received}")

#     # Test 2: Prepend and append with flips
#     bv = BitVector()
#     bv.append(1)
#     bv.flip_all_bits()
#     bv.prepend(0)
#     bv.append(1)
#     expected = "011"
#     received = str(bv)
#     print(f"Test 2 - Expected: {expected}, Received: {received}")

#     # Test 3: Multiple prepends and appends with reverse and flip
#     bv = BitVector()
#     bv.append(1)
#     bv.prepend(0)
#     bv.reverse()
#     bv.append(1)
#     bv.prepend(1)
#     bv.flip_all_bits()
#     expected = "0010"
#     received = str(bv)
#     print(f"Test 3 - Expected: {expected}, Received: {received}")

#     # Test 4: Testing shift operations
#     bv = BitVector()
#     bv.append(1)
#     bv.append(0)
#     bv.prepend(0)
#     bv.prepend(1)
#     bv.shift(1)
#     expected = "0010"
#     received = str(bv)
#     print(f"Test 4 - Expected: {expected}, Received: {received}")

#     # Test 5: Testing rotate operations
#     bv = BitVector()
#     bv.append(1)
#     bv.append(0)
#     bv.append(1)
#     bv.rotate(1)
#     expected = "110"
#     received = str(bv)
#     print(f"Test 5 - Expected: {expected}, Received: {received}")

def test_bitvector():
    bv = BitVector()
    bv.append(0)
    bv.append(1)
    print(bv)





  





# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Data Structures")

    parser.add_argument("--linkedlist", action="store_true", help="Test your linked list.")
    parser.add_argument("--dynamicarray", action="store_true", help="Test your dynamic array.")
    parser.add_argument("--bitvector", action="store_true", help="Test your bit vector.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.linkedlist:
        test_linked_list()

    if args.dynamicarray:
        test_dynamic_array()

    if args.bitvector:
        test_bitvector()
    





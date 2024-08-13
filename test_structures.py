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

##test i wrote
def test_finding_element():

    #Initialsing list
    linked_list = DoublyLinkedList()
    
    # assert linked_list.find_element("test") == True, "Test failed: Found element in empty list"

    linked_list.insert_to_front("david")
    linked_list.insert_to_front("araba")

    assert linked_list.find_element("araba") == False, "Test failed: The word is in the list"

def test_str_rep():

    linked_list = DoublyLinkedList()

    # print(str(linked_list)) #should print is empty 

    linked_list.insert_to_front("araba")
    linked_list.insert_to_front("david")
    linked_list.insert_to_back("is the best")
    print(str(linked_list))

    print(linked_list.get_head())

    linked_list.reverse()
    print(linked_list.get_head())

    # linked_list.reverse()
    # print(str(linked_list))
    # linked_list.insert_to_back("yo")
    # print(str(linked_list))
    # print("tail is: " + linked_list.get_tail())
    

def test_find_and_remove():
    linked_list = DoublyLinkedList()
    linked_list.insert_to_front("jdsasd")
    linked_list.insert_to_front("hello")
    linked_list.insert_to_front("david")

    linked_list.find_and_remove_element("hello")

    print(str(linked_list))

def test_reverse():
    linked_list = DoublyLinkedList() 
    linked_list.insert_to_back(5)
    linked_list.insert_to_back(4)
    linked_list.insert_to_back(3)
    linked_list.insert_to_back(2)
    linked_list.insert_to_back(1)

    print(str(linked_list))

    linked_list.reverse()

    print(str(linked_list))

def test_dynamic_array():
    """
    A simple set of tests for the dynamic array implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Dynamic Array Tests ====")

def test_bitvector():
    """
    A simple set of tests for the bit vector implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Bit Vector Tests ====")

def test_array_string():
    my_array = DynamicArray()
    
    my_array.append(2)
    my_array.append(3)
    my_array.append(7)
    my_array.prepend(8)
    
    print("array before reverse: " + str(my_array))
    y = my_array.get_at(0)
    print(y)
    
    my_array.reverse()
    print("array after reverse: " + str(my_array))
    x = my_array.get_at(0)
    print(x)
    


    
    # print(my_array)
    # print(my_array.get_size())

    # my_array.remove(1)
    # print(my_array)

    

  


   




 

    

    # my_array.remove(2)
    # print(str(my_array))

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Data Structures")

    parser.add_argument("--linkedlist", action="store_true", help="Test your linked list.")
    parser.add_argument("--dynamicarray", action="store_true", help="Test your dynamic array.")
    parser.add_argument("--findelement", action="store_true", help="Test find element in linked list.")
    parser.add_argument("--strmethod", action="store_true", help="Test __str__ method in linked list.")
    parser.add_argument("--findremove", action="store_true", help="Test find and remove.")
    parser.add_argument("--bitvector", action="store_true", help="Test your bit vector.")
    parser.add_argument("--reverse", action="store_true", help="Test reverse" )
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    parser.add_argument("--arraystr", action="store_true", help="Test your array string.")
    
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
    
    if args.findelement:
        test_finding_element()

    if args.strmethod:
        test_str_rep()
    
    if args.findremove:
        test_find_and_remove()

    if args.reverse:
        test_reverse()

    if args.arraystr:
        test_array_string()



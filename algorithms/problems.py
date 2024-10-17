"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

 Each problem will be assessed on three sets of tests:

1. "It works":
       Basic inputs and outputs, including the ones peovided as examples, with generous time and memory restrictions.
       Large inputs will not be tested here.
       The most straightforward approach will likely fit into these restrictions.

2. "Exhaustive":
       Extensive testing on a wide range of inputs and outputs with tight time and memory restrictions.
       These tests won't accept brute force solutions, you'll have to apply some algorithms and optimisations.

 3. "Welcome to COMP3506":
       Extensive testing with the tightest possible time and memory restrictions
       leaving no room for redundant operations.
       Every possible corner case will be assessed here as well.

There will be hidden tests in each category that will be published only after the assignment deadline.

You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
from structures.entry import Entry, Compound, Offer
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList
from structures.bit_vector import BitVector
from structures.graph import Graph, LatticeGraph
from structures.map import Map
from structures.pqueue import PriorityQueue
from structures.bloom_filter import BloomFilter
from structures.huffman_node import HuffmanNode


def maybe_maybe_maybe(database: list[str], query: list[str]) -> list[str]:
    """
    Task 3.1: Maybe Maybe Maybe

    @database@ is an array of k-mers in our database.
    @query@ is an array of k-mers we want to search for.

    Return a list of query k-mers that are *likely* to appear in the database.

    Limitations:
        "It works":
            @database@ contains up to 1000 elements;
            @query@ contains up to 1000 elements.

        "Exhaustive":
            @database@ contains up to 100'000 elements;
            @query@ contains up to 100'000 elements.

        "Welcome to COMP3506":
            @database@ contains up to 1'000'000 elements;
            @query@ contains up to 500'000 elements.

    Each test will run over three false positive rates. These rates are:
        fp_rate = 10%
        fp_rate = 5%
        fp_rate = 1%.

    You must pass each test in the given time limit and be under the given
    fp_rate to get the associated mark for that test.
    """
    answer = []

    max_keys = len(database)

    database_bloom = BloomFilter(max_keys)

    for item in database:
        database_bloom.insert(item)

    for item in query:
        if database_bloom.contains(item):
            answer.append(item)

    return answer


def dora(graph: Graph, start: int, symbol_sequence: str,
         ) -> tuple[BitVector, list[Entry]]:
    """
    Task 3.2: Dora and the Chin Bicken

    @graph@ is the input graph G; G might be disconnected; each node contains
    a single symbol in the node's data field.
    @start@ is the integer identifier of the start vertex.
    @symbol_sequence@ is the input sequence of symbols, L, with length n.
    All symbols are guaranteed to be found in G. 

    Return a BitVector encoding symbol_sequence via a minimum redundancy code.
    The BitVector should be read from index 0 upwards (so, the first symbol is
    encoded from index 0). You also need to return your codebook as a
    Python list of unique Entries. The Entry key should correspond to the
    symbol, and the value should be a string. More information below.

    Limitations:
        "It works":
            @graph@ has up to 1000 vertices and up to 1000 edges.
            the alphabet consists of up to 26 characters.
            @symbol_sequence@ has up to 1000 characters.

        "Exhaustive":
            @graph@ has up to 100'000 vertices and up to 100'000 edges.
            the alphabet consists of up to 1000 characters.
            @symbol_sequence@ has up to 100'000 characters.

        "Welcome to COMP3506":
            @graph@ has up to 1'000'000 vertices and up to 1'000'000 edges.
            the alphabet consists of up to 300'000 characters.
            @symbol_sequence@ has up to 1'000'000 characters.

    """
    coded_sequence = BitVector()

    """
    list of Entry objects, each entry has key=symbol, value=str. The str
    value is just an ASCII representation of the bits used to encode the
    given key. For example: x = Entry("c", "1101")
    """
    codebook = []

    visited = [False] * len(graph._nodes)
    gene_count = Map()

    queue = DoublyLinkedList()
    queue.insert_to_back(start)
    visited[start] = True

    while queue.get_size() > 0:
        current_node_id = queue.remove_from_front()
        current_node = graph.get_node(current_node_id)
        current_symbol = current_node.get_data()

        count = gene_count.find(current_symbol)

        if count is not None:
            gene_count.insert_kv(current_symbol, count + 1)
        else:
            gene_count.insert_kv(current_symbol, 1)

        neighbours = graph.get_neighbours(current_node_id)

        for neighbour in neighbours:
            neighbour_id = neighbour.get_id()
            if not visited[neighbour_id]:
                queue.insert_to_back(neighbour_id)
                visited[neighbour_id] = True

    huffman_pq = PriorityQueue()

    for genes in gene_count.iterate_over_entries():
        symbol = genes.get_key()
        frequency = genes.get_value()

        huffman_node = HuffmanNode(symbol, frequency)
        huffman_pq.insert(frequency, huffman_node)

    if huffman_pq.is_empty():
        root = None
    else:
        while huffman_pq.get_size() > 1:
            left_node = huffman_pq.remove_min()
            right_node = huffman_pq.remove_min()
            combined_frequency = left_node._frequency + right_node._frequency
            new_node = HuffmanNode(None, combined_frequency)
            new_node._left = left_node
            new_node._right = right_node
            huffman_pq.insert(combined_frequency, new_node)
        root = huffman_pq.remove_min()

    codebook_map = Map()

    def generate_codes(node, current_code):
        if node is None:
            return
        if node._symbol is not None:
            code_entry = Entry(node._symbol, current_code)
            codebook.append(code_entry)
            codebook_map.insert_kv(node._symbol, current_code)
            return
        generate_codes(node._left, current_code + '0')
        generate_codes(node._right, current_code + '1')

    generate_codes(root, '')

    for symbol in symbol_sequence:
        code = codebook_map.find(symbol)
        if code is None:
            continue
        for char_bit in code:
            bit = int(char_bit)
            coded_sequence.append(bit)

    return (coded_sequence, codebook)


def chain_reaction(compounds: list[Compound]) -> int:
    """
    Task 3.3: Chain Reaction

    @compounds@ is a list of Compound types, see structures/entry.py for the
    definition of a Compound. In short, a Compound has an integer x and y
    coordinate, a floating point radius, and a unique integer representing
    the compound identifier.

    Return the compound identifier of the compound that will yield the
    maximal number of compounds in the chain reaction if set off. If there
    are ties, return the one with the smallest identifier.

    Limitations:
        "It works":
            @compounds@ has up to 100 elements

        "Exhaustive":
            @compounds@ has up to 1000 elements

        "Welcome to COMP3506":
            @compounds@ has up to 10'000 elements

    """

    def compounds_overlap(compound1: Compound, compound2: Compound) -> bool:
        radius_squared = compound1.get_radius() ** 2
        x1, y1 = compound1.get_coordinates()
        x2, y2 = compound2.get_coordinates()
        distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2

        return distance_squared <= radius_squared

    if not compounds:
        return -1

    maximal_compound_count = 0
    maximal_compound_id = compounds[0].get_compound_id()

    for i, compound in enumerate(compounds):
        queue = DynamicArray()
        queue.append(compound)
        visited = [False] * len(compounds)
        visited[i] = True

        local_impact_count = 1

        while not queue.is_empty():
            current_compound = queue.remove_at(0)

            for j, neighbour in enumerate(compounds):
                if not visited[j] and compounds_overlap(current_compound, neighbour):
                    visited[j] = True
                    queue.append(neighbour)
                    local_impact_count += 1

        if local_impact_count > maximal_compound_count:
            maximal_compound_count = local_impact_count
            maximal_compound_id = compound.get_compound_id()
        elif local_impact_count == maximal_compound_count:
            if compound.get_compound_id() < maximal_compound_id:
                maximal_compound_id = compound.get_compound_id()

    return maximal_compound_id


def labyrinth(offers: list[Offer]) -> tuple[int, int]:
    """
    Task 3.4: Labyrinth

    @offers@ is a list of Offer types, see structures/entry.py for the
    definition of an Offer. In short, an Offer stores n (number of nodes),
    m (number of edges), and k (diameter) of the given Labyrinth. Each
    Offer also has an associated cost, and a unique offer identifier.

    Return the offer identifier and the associated cost for the cheapest
    labyrinth that can be constructed from the list of offers. If there
    are ties, return the one with the smallest identifier. 
    You are guaranteed that all offer ids are distinct.

    Limitations:
        "It works":
            @offers@ contains up to 1000 items.
            0 <= n <= 1000
            0 <= m <= 1000
            0 <= k <= 1000

        "Exhaustive":
            @offers@ contains up to 100'000 items.
            0 <= n <= 10^6
            0 <= m <= 10^6
            0 <= k <= 10^6

        "Welcome to COMP3506":
            @offers@ contains up to 5'000'000 items.
            0 <= n <= 10^42
            0 <= m <= 10^42
            0 <= k <= 10^42

    """

    def valid_offer(offer: Offer) -> bool:
        n = offer.get_num_nodes()
        m = offer.get_num_edges()
        k = offer.get_diameter()

        if (m >= n - 1 and m < (n * (n - 1)) / 2 and k > n - m):
            return True

        return False

    best_offer_id = -1
    best_offer_cost = float('inf')

    for offer in offers:
        if valid_offer(offer):
            if offer.get_cost() < best_offer_cost:
                best_offer_cost = offer.get_cost()
                best_offer_id = offer.get_offer_id()
            elif offer.get_cost() == best_offer_cost:
                if offer.get_offer_id() < best_offer_id:
                    best_offer_id = offer.get_offer_id()

    # print(best_offer_id, best_offer_cost)
    return (best_offer_id, best_offer_cost)

"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
from structures.entry import Entry
from structures.dynamic_array import DynamicArray
from structures.graph import Graph, LatticeGraph
from structures.pqueue import PriorityQueue
from structures.linked_list import DoublyLinkedList


def bfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
) -> tuple[DynamicArray, DynamicArray]:
    """
    Task 2.1: Breadth First Search

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()
    # Queue
    queue = DoublyLinkedList()
    # Enqueue origin as the first node to be visited
    queue.insert_to_back(origin)

    visited = DynamicArray()

    num_vertices = len(graph._nodes)

    visited.allocate(num_vertices, False)
    parent = DynamicArray()
    parent.allocate(num_vertices, None)

    visited[origin] = True
    while queue.get_size() > 0:
        current_node = queue.remove_from_front()

        visited_order.append(current_node)

        if current_node == goal:
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]

            for i in range(path.get_size() // 2):
                temp = path[i]
                path[i] = path[path.get_size() - 1 - i]
                path[path.get_size() - 1 - i] = temp
            break

        current_node_neighbours = graph.get_neighbours(current_node)

        for neighbour in current_node_neighbours:
            neighbour_id = neighbour.get_id()
            if not visited[neighbour_id]:
                queue.insert_to_back(neighbour_id)
                visited[neighbour_id] = True
                parent[neighbour_id] = current_node

    # Return the path and the visited nodes list
    return (path, visited_order)


def dijkstra_traversal(graph: Graph, origin: int) -> DynamicArray:
    """
    Task 2.2: Dijkstra Traversal

    @param: graph
      The *weighted* graph to process (POSW graphs)
    @param: origin
      The ID of the node from which to start traversal.

    @returns: DynamicArray containing Entry types.
      The Entry key is a node identifier, Entry value is the cost of the
      shortest path to this node from the origin.

    NOTE: Dijkstra does not work (by default) on LatticeGraph types.
    This is because there is no inherent weight on an edge of these
    graphs. It should of course work where edge weights are uniform.
    """
    valid_locations = DynamicArray()  # This holds your answers
    num_vertices = len(graph._nodes)

    # First thing in queue is origin with distance 0
    queue = PriorityQueue()
    queue.insert(0, origin)

    # Will keep track of the shortest distance of each node from the origin
    distances = DynamicArray()
    # Initialise distances: set all to infinity, except the origin which is 0
    distances.allocate(num_vertices, float('inf'))
    distances[origin] = 0  # map maybe

    # Will keep track of what edges visited
    visited = DynamicArray()
    # Initially false
    visited.allocate(num_vertices, False)

    while not queue.is_empty():

        current_node = queue.get_min_value()
        queue.remove_min()

        if visited[current_node]:
            continue

        visited[current_node] = True

        current_node_neighbour = graph.get_neighbours(current_node)

        for neighbour_node, edge_weight in current_node_neighbour:
            neighbour_id = neighbour_node.get_id()
            # Potential new shortest path from the origin to neighbour_id via current_node
            new_distance = distances[current_node] + edge_weight

            if new_distance < distances[neighbour_id]:
                distances[neighbour_id] = new_distance
                queue.insert(new_distance, neighbour_id)

    for node_id in range(num_vertices):
        if distances[node_id] != float('inf'):
            valid_locations.append(
                Entry(key=node_id, value=distances[node_id]))

    # Return the DynamicArray containing Entry types
    return valid_locations


def dfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
) -> tuple[DynamicArray, DynamicArray]:
    """
    Task 2.3: Depth First Search **** COMP7505 ONLY ****
    COMP3506 students can do this for funsies.

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.

    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()
    # Stack for DFS
    stack = DynamicArray()
    # Append origin to begin DFS
    stack.append(origin)

    visited = DynamicArray()

    num_vertices = len(graph._nodes)
    visited.allocate(num_vertices, False)
    parent = DynamicArray()
    parent.allocate(num_vertices, None)

    visited[origin] = True

    while stack.get_size() > 0:
        current_node = stack[stack.get_size() - 1]
        stack.remove_at(stack.get_size() - 1)

        visited_order.append(current_node)

        if current_node == goal:
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]

            for i in range(path.get_size() // 2):
                temp = path[i]
                path[i] = path[path.get_size() - 1 - i]
                path[path.get_size() - 1 - i] = temp
            break

        current_node_neighbours = graph.get_neighbours(current_node)

        for neighbour in current_node_neighbours:
            neighbour_id = neighbour.get_id()
            if not visited[neighbour_id]:
                stack.append(neighbour_id)
                visited[neighbour_id] = True
                parent[neighbour_id] = current_node

    # Return the path and the visited nodes list
    return (path, visited_order)

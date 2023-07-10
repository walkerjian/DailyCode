def is_minimally_connected(graph):
    """
    This function checks if a graph is minimally connected.

    :param graph: The graph represented as a dictionary.
    :return: True if the graph is minimally connected, False otherwise.
    """
    # Go through each node in the graph
    for node in graph:
        # Check the number of connections this node has
        if len(graph[node]) > 2:
            # If the node has more than two connections, it means that removing any edge would still leave the graph connected
            return False
        elif len(graph[node]) == 2 and node != list(graph.keys())[0]:
            # If a node (except the first node) has exactly two connections, the graph is not minimally connected
            return False
    # If we've gone through all the nodes and none have more than two connections, the graph is minimally connected
    return True
# Test 1: A minimally connected graph (a straight line)
graph = {1: [2], 2: [1, 3], 3: [2]}
print(is_minimally_connected(graph))  # Should print: True

# Test 2: A minimally connected graph (a binary tree)
graph = {1: [2, 3], 2: [1], 3: [1]}
print(is_minimally_connected(graph))  # Should print: True

# Test 3: A non-minimally connected graph
graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
print(is_minimally_connected(graph))  # Should print: False

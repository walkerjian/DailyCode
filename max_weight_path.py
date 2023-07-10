def max_weight_path(triangle):
    """
    This function calculates the maximum weight path in a triangle.
    
    Parameters:
    triangle (list of lists): The triangle represented as a list of lists of integers.
    
    Returns:
    int: The maximum weight path in the triangle.
    """

    # If the triangle is empty, return 0
    if not triangle:
        return 0

    # Start from the second last row and go up
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Calculate the maximum sum of each path
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # The maximum weight path is at the top of the triangle
    return triangle[0][0]
assert max_weight_path([[1], [2, 3], [1, 5, 1]]) == 9
assert max_weight_path([[1], [2, 1], [1, 2, 3]]) == 6
assert max_weight_path([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) == 20
assert max_weight_path([[5], [9, 6], [4, 6, 8], [0, 7, 1, 5]]) == 27

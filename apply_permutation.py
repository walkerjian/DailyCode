def apply_permutation(array, permutation):
    """
    Applies a permutation to a given array.

    :param array: The array to be permuted.
    :param permutation: The permutation to be applied.
    :return: The permuted array.
    """
    # Create a new list to store the result
    result = [None] * len(array)
    for i, p in enumerate(permutation):
        result[p] = array[i]
    return result
def test_apply_permutation():
    """
    Tests the apply_permutation function with some example cases.
    """
    assert apply_permutation(["a", "b", "c"], [2, 1, 0]) == ["c", "b", "a"]
    assert apply_permutation([1, 2, 3], [2, 0, 1]) == [2, 3, 1]
    assert apply_permutation(["apple", "banana", "cherry"], [1, 2, 0]) == ["banana", "cherry", "apple"]

# Running the tests
test_apply_permutation()

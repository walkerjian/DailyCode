def find_first_recurring_char(s):
    """
    This function finds the first recurring character in a given string.

    Arguments:
    s -- the input string

    Returns:
    The first recurring character, or None if there is no such character.
    """

    # We'll keep track of the characters we've seen so far using a set.
    # Sets in Python are like lists, but they can't contain duplicate values,
    # and checking if a value is in a set is faster than checking if it's in a list.
    seen_chars = set()

    # We'll iterate over each character in the string.
    for char in s:
        # If we've already seen this character, it's the first recurring one,
        # so we return it.
        if char in seen_chars:
            return char

        # Otherwise, we add it to the set of seen characters.
        seen_chars.add(char)

    # If we've gone through the whole string and haven't found a recurring character,
    # we return None.
    return None

def tests():
    """
    This function tests the find_first_recurring_char function.
    """

    # We're going to test a few different cases.

    # First, a string where the first recurring character is in the middle.
    assert find_first_recurring_char("acbbac") == "b"

    # Second, a string where the first recurring character is at the end.
    assert find_first_recurring_char("abcdefa") == "a"

    # Third, a string with no recurring characters.
    assert find_first_recurring_char("abcdef") == None

    # Finally, an empty string. This should also return None.
    assert find_first_recurring_char("") == None

    print("All tests passed!")

# We call the test function
tests()

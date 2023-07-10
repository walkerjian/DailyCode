'''
Problem Statement:

Given a number represented by a list of digits, find the next greater permutation of a number, 
in terms of lexicographic ordering. If there is not greater permutation possible, 
return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. 
The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
'''

def next_permutation_integer(n):
    '''
    Function that accepts an integer, converts it into a list of digits, applies the next permutation to that list,
    then converts the list back into an integer and returns the result.
    '''
    # Convert the integer into a list of digits
    nums = [int(i) for i in str(n)]
    
    # Apply the next permutation to the list of digits
    next_permutation(nums)
    
    # Convert the list of digits back into an integer
    next_permutation_num = int(''.join(map(str, nums)))
    
    # Returns the next permutation of the number n, in integer form
    return next_permutation_num

def next_permutation(nums):
    '''
    Function that modifies a list of digits in-place to produce the next lexicographically greater permutation. 
    If no such permutation is possible (i.e., the list is already in descending order), 
    it reverses the list to produce the lexicographically smallest permutation.
    '''
    # Find the largest index i such that nums[i] < nums[i + 1]. 
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    # If no such index exists, the permutation is sorted in descending order, 
    # reverse it to ascending order and return.
    if i <= 0:
        nums.reverse()
        return nums
    
    # nums[i - 1] is the pivot.
    # Find rightmost element that exceeds the pivot
    j = len(nums) - 1
    while nums[j] <= nums[i - 1]:
        j -= 1
    
    # Swap the pivot with nums[j]
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    
    # Reverse the suffix starting from nums[i], so the list is now in ascending order
    nums[i : ] = nums[len(nums) - 1 : i - 1 : -1]
    return nums

# Test the function with a set of test cases
test_cases = [123, 132, 321, 54321, 23415, 987654321]

for n in test_cases:
    print(f"Original number: {n}")
    result = next_permutation_integer(n)
    print(f"Next permutation: {result}\n")

test_cases = [123, 132, 321, 54321, 23415, 987654321, 2222, 11111, 5432, 1]

for n in test_cases:
    print(f"Original number: {n}")
    result = next_permutation_integer(n)
    print(f"Next permutation: {result}\n")

assert next_permutation_integer(123) == 132
assert next_permutation_integer(132) == 213
assert next_permutation_integer(321) == 123  # Edge case: Descending order
assert next_permutation_integer(54321) == 12345  # Edge case: Descending order
assert next_permutation_integer(23415) == 23451
assert next_permutation_integer(987654321) == 123456789  # Edge case: Descending order
assert next_permutation_integer(2222) == 2222  # Edge case: Same digits
assert next_permutation_integer(11111) == 11111  # Edge case: Same digits
assert next_permutation_integer(5432) == 12345  # Edge case: Descending order
assert next_permutation_integer(1) == 1  # Edge case: Single digit

import unittest

class TestNextPermutationInteger(unittest.TestCase):
    def test_next_permutation_integer(self):
        self.assertEqual(next_permutation_integer(123), 132)
        self.assertEqual(next_permutation_integer(132), 213)
        self.assertEqual(next_permutation_integer(321), 123)  # Edge case: Descending order
        self.assertEqual(next_permutation_integer(54321), 12345)  # Edge case: Descending order
        self.assertEqual(next_permutation_integer(23415), 23451)
        self.assertEqual(next_permutation_integer(987654321), 123456789)  # Edge case: Descending order
        self.assertEqual(next_permutation_integer(2222), 2222)  # Edge case: Same digits
        self.assertEqual(next_permutation_integer(11111), 11111)  # Edge case: Same digits
        self.assertEqual(next_permutation_integer(5432), 12345)  # Edge case: Descending order
        self.assertEqual(next_permutation_integer(1), 1)  # Edge case: Single digit

if __name__ == "__main__":
    unittest.main()


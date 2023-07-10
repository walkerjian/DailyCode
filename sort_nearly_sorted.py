# Import the heapq module. This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
import heapq

# Define the main function to sort a nearly sorted array. The function accepts the array and the distance k as input.
def sort_k_messed_array(arr, k):

    # Initialize a min-heap with the first k + 1 elements of the array. In Python, ordinary lists can be used as min-heaps.
    heap = arr[:k + 1]

    # The heapify function transforms the list into a heap, in-place, in linear time.
    heapq.heapify(heap)

    # For every element in the array starting from the index k + 1,
    for i in range(k + 1, len(arr)):

        # We take the smallest element from the heap (which is the root and always contains the smallest element in a min-heap)
        # and replace it with the i-th element of the array.
        arr[i - (k + 1)] = heapq.heappop(heap)

        # The heappush function pushes the value item onto the heap, maintaining the heap invariant.
        heapq.heappush(heap, arr[i])

    # Place all remaining elements from the heap to the array.
    for i in range(len(arr) - k - 1, len(arr)):

        # The heappop function pops and returns the smallest element from the heap.
        arr[i] = heapq.heappop(heap)

    # Return the sorted array.
    return arr


# Testing the function with a nearly sorted array and k = 2
print(sort_k_messed_array([6, 5, 3, 2, 8, 10, 9], 3))  # Expected output: [2, 3, 5, 6, 8, 9, 10]

#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
#Note: The kth smallest element is determined based on the sorted order of the array.

import heapq

class Solution:
    def kthSmallest(self, arr, k):
        """
        arr : given array
        k : find the kth smallest element
        """
        # Create a max heap to store the k smallest elements seen so far
        # We use negative values because Python's heapq is a min-heap
        max_heap = []
        
        for num in arr:
            heapq.heappush(max_heap, -num)
            
            # If the heap size exceeds k, remove the largest element
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # The root of the max_heap is the kth smallest element
        return -max_heap[0]

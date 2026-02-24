#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        # Initialize current sum and minimum length
        curr_sum = 0
        min_len = n + 1
        
        # Initialize starting index
        left = 0
        
        # Iterate over the array
        for right in range(n):
            # Keep adding array elements while current sum is <= x
            curr_sum += arr[right]
            
            # Once current sum becomes greater than x
            while curr_sum > x:
                # Update minimum length if this window is smaller
                min_len = min(min_len, right - left + 1)
                
                # Shrink the window from the left to find a smaller subarray
                curr_sum -= arr[left]
                left += 1
                
        # If no such subarray is found, return 0
        return min_len if min_len <= n else 0

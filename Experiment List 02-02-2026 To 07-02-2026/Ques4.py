#Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find
#the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

class Solution:
    def minSwap(self, arr, k):
        # Calculate N inside the function to match GFG's driver code
        n = len(arr)
        
        # 1. Count all elements <= k (these are our "good" elements)
        good = 0
        for x in arr:
            if x <= k:
                good += 1
        
        # If no elements or only one element <= k, no swaps are needed
        if good <= 1:
            return 0
        
        # 2. Count "bad" elements (> k) in the initial window of size 'good'
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        # Initial answer is the number of bad elements in the first window
        ans = bad
        
        # 3. Slide the window through the rest of the array
        for i in range(good, n):
            # Element leaving the window (at the back)
            if arr[i - good] > k:
                bad -= 1
            
            # Element entering the window (at the front)
            if arr[i] > k:
                bad += 1
            
            # 4. The number of swaps needed for any window is the count of 'bad' elements
            ans = min(ans, bad)
            
        return ans

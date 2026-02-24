#Given an array arr[] denoting heights of n towers and a positive integer k.
#For each tower, you must perform exactly one of the following operations exactly once.
#Increase the height of the tower by k
#Decrease the height of the tower by k
#Find out the minimum possible difference between the height of the shortest and tallest towers
#after you have modified each tower.
#You can find a slight modification of the problem here.
#Note: It is compulsory to increase or decrease the height by k for each tower. After the operation,the resultant array should not contain any negative integers.


class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
            
        # 1. Sort the array
        arr.sort()
        
        # 2. Initial difference (without any modifications)
        ans = arr[n-1] - arr[0]
        
        # 3. Greedy approach: Try every possible "split point"
        # We increase everything before 'i' and decrease everything from 'i' onwards
        for i in range(1, n):
            # The problem states height cannot be negative
            if arr[i] - k < 0:
                continue
            
            # After modification, the new potential minimum and maximum:
            current_min = min(arr[0] + k, arr[i] - k)
            current_max = max(arr[i-1] + k, arr[n-1] - k)
            
            ans = min(ans, current_max - current_min)
            
        return ans

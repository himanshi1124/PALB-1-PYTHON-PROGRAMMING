#Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -i. Each student gets exactly one packet. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.
class Solution:
    def findMinDiff(self, arr, M):
        n = len(arr)
        
        if M == 0 or n == 0:
            return 0
        
        if M > n:
            return -1
        
        arr.sort()
        minDiff = float('inf')
        
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            minDiff = min(minDiff, diff)
        
        return minDiff

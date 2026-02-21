#Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that - i. Each student gets exactly one packet. ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.
class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        min_len = float('inf')
        curr_sum = 0
        start = 0

        for end in range(n):
            curr_sum += arr[end]

            # Shrink window while sum > x
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1

        if min_len == float('inf'):
            return 0

        return min_len

#Given an array arr[] of positive integers, where each value represents the number of
#chocolates in a packet. Each packet can have a variable number of chocolates. There
#are m students, the task is to distribute chocolate packets among m students such that -
#i. Each student gets exactly one packet.
#ii. The difference between maximum number of chocolates given to a student and
#minimum number of chocolates given to a student is minimum and return that minimum possible difference.

class Solution:
    def findMinDiff(self, A, M):
        # Calculate N inside the function
        N = len(A)
        
        # 1. Edge Case: If there are no chocolates or students
        if M == 0 or N == 0:
            return 0
        
        # 2. Sort the array
        A.sort()
        
        # 3. Edge Case: If students are more than available packets
        if N < M:
            return -1
        
        # 4. Initialize min_diff with a very large value
        min_diff = float('inf')
        
        # 5. Sliding Window
        # Traverse the sorted list and check windows of size M
        for i in range(N - M + 1):
            # Calculate difference between the last and first element of the window
            current_diff = A[i + M - 1] - A[i]
            
            # Update the global minimum difference
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff

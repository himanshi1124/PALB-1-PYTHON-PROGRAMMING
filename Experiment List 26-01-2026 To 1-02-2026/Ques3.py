#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        # 1. Initialize two pointers
        # 'i' starts from the end of the first array (largest of a)
        # 'j' starts from the beginning of the second array (smallest of b)
        i = n - 1
        j = 0
        
        # 2. Compare elements and swap if they are in the wrong order
        # We want all elements in 'a' to be smaller than elements in 'b'
        while i >= 0 and j < m:
            if a[i] > b[j]:
                # Swap the larger element from 'a' with the smaller element from 'b'
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                # Since both arrays are sorted, if a[i] <= b[j], 
                # then all elements before 'i' are already smaller than all after 'j'
                break
        
        # 3. Sort both arrays individually to maintain internal order
        a.sort()
        b.sort()

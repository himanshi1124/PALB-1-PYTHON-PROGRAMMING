#You are given two arrays a[] and b[], return the Union of both the arrays in any order.

class Solution:    
    def findUnion(self, a, b):
        # code here
        union_set = set(a).union(set(b))
        return list(union_set)

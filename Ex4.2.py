#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # choose
                current.append(candidates[i])
                
                # stay at i (not i+1) because reuse allowed
                backtrack(i, current, remaining - candidates[i])
                
                # undo choice
                current.pop()
        
        backtrack(0, [], target)
        return result

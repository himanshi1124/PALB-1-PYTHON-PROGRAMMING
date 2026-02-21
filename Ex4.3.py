#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # Skip duplicates at same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Prune (since sorted)
                if candidates[i] > remaining:
                    break
                
                current.append(candidates[i])
                
                # Move to next index (no reuse allowed)
                backtrack(i + 1, current, remaining - candidates[i])
                
                current.pop()
        
        backtrack(0, [], target)
        return result

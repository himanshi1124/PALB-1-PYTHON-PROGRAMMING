#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 

class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[nums[i]] = i

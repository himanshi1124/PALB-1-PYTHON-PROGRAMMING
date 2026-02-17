#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
class Solution:
    def findDuplicate(self, nums):
        
        # Step 1: Find intersection point
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # Step 2: Find entrance to cycle
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

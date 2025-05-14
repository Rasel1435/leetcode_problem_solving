"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


nums = [1,2,3,4,1]
class Solution:
    def containsDuplicate(self, nums):
        busket = set()
        
        for n in nums:
            if n in busket:
                return True
            busket.add(n)
        return False
    
sol = Solution()
result = sol.containsDuplicate(nums)
print(result)



"""
Step-by-step: Breakdown this code

busket = set() # empty set

Loop over: 1 → not in set → add → busket = {1}

Next: 2 → not in set → add → busket = {1, 2} 

Next: 3 → not in set → add → busket = {1, 2, 3}

Next: 4 → not in set → add → busket = {1, 2, 3, 4}

Next: 1 → already in set → return True

"""
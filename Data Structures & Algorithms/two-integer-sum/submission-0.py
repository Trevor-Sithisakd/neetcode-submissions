class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if target - one number = num that is in nums how to get integer
        # brute force two loops check if they add if they do return i,j 
        # hash map it loop through check if the complement exists if not add it to the hash map and then continue 
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i] # ordered for smaller index already
            seen[num] = i
        
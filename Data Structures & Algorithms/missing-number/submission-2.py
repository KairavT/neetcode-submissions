class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0  
        nums_set = set(nums)

        while target < len(nums):
            if target not in nums_set:
                return target
            target += 1
        return target 
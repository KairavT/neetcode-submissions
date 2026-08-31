class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]== target:
                return i
            elif target < nums[i]:
                return -1
        return -1
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            random_ = random.choice(nums)
            if nums.count(random_) > n//2:
                return random_
            
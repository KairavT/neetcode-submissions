class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        lens = set()


        max_len = 0
        for num in nums:
            max_len_loop = 1
            if (num - 1) in num_set:
                continue
            else:
                while num + max_len_loop in num_set:
                    max_len_loop += 1
            max_len = max(max_len, max_len_loop)
        return max_len
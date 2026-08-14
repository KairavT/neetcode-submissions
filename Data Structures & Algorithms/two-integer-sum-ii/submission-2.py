class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) -1
        
        cur_sum = numbers[p1] + numbers[p2]

        while p1 < p2:
            cur_sum = numbers[p1] + numbers[p2]
            if target < cur_sum:
                p2 -= 1
            elif target > cur_sum:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
        return [p1 + 1, p2 + 1]
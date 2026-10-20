class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            t = temperatures[i]
            while stack and t > stack[-1][1]:
                stack_i, stack_temp = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((i, t))
        return res
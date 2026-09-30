class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for o in range(len(ops)):
            if ops[o] == '+':
                stack.append(stack[-1] + stack[-2])
            elif ops[o] == 'D':
                stack.append(2 * stack[-1])
            elif ops[o] == 'C':
                stack.pop()
            else:
                stack.append(int(ops[o]))

        return sum(stack)
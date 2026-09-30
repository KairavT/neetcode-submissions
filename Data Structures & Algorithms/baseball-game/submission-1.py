class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for o in range(len(ops)):
            if ops[o] == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif ops[o] == 'D':
                stack.append(2 * int(stack[-1]))
            elif ops[o] == 'C':
                stack.pop()
            else:
                stack.append(ops[o])

        return sum([int(n) for n in stack])
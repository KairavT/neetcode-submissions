class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {
            '(':')',
            '{':'}',
            '[':']'
        }
        brackets  = []
        for char in s:
            if char in open_close:
                brackets.append(char)
            elif not brackets:
                return False
            else:
                if char != open_close[brackets.pop()]:
                    return False
        if brackets:
            return False
        else: 
            return True
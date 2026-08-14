class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_1 = 0
        p_2 = len(s) -1
        alphanumeric=\
        "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        if len(s) <= 1: return True
        while p_2 >= p_1:
            while s[p_2] not in alphanumeric and p_2 > p_1:
                    p_2 -= 1
            while s[p_1] not in alphanumeric and p_2 > p_1:
                    p_1 += 1

            if s[p_2].lower() != s[p_1].lower():
                    return False
            else:
                    p_1 += 1
                    p_2 -= 1
        return True

        
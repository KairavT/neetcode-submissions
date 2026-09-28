class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            
            letter_count = [0]*26

            for i in range(len(s)):
                letter_count[ord(s[i]) - ord('a')] += 1
                letter_count[ord(t[i]) - ord('a')] -= 1
            
            for num in letter_count:
                if num != 0:
                    return False
            return True


            


                
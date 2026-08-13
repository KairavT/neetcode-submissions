class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            t_dict = {}
            s_dict = {}
            if len(s) != len(t):
                return False
                
            for i in range(len(s)):
                if s[i] in s_dict:
                    s_dict[s[i]] += 1
                else:
                    s_dict[s[i]] = 1

                if t[i] in t_dict:
                    t_dict[t[i]] += 1
                else:
                    t_dict[t[i]] = 1
            
            return t_dict == s_dict

                
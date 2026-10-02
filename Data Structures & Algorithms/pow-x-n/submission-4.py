class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == 0:
            return 0
        ans = 1

        nn = abs(n)
        while nn > 0:
            if nn % 2 ==1:
                ans *= x
            x *= x
            nn//=2
        if n > 0:
            return ans
        else:
            return 1/ans

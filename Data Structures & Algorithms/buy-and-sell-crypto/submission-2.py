class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        curmin = 100

        for price in prices:
            if price < curmin:
                curmin = price
            if price - curmin > mp:
                mp = price - curmin

        return mp






        
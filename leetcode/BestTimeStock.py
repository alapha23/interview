
class Solution:
    def maxProfit(self, prices: list) -> int:
        s = 0
        g = 0
        b = prices[0]
        for p in prices:
            s = max(0, p-b)
            b = min(p, b)
            g = max(g, s)
        return g

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

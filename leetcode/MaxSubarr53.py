
class Solution:
    def maxSubArray(self, nums: list) -> int:
        s = 0
        g = -10000 * len(nums)
        flag = 0
        for n in nums:
            if n >= 0:
                flag = 1
            s = max(0, s+n)
            g = max(s, g)
        if flag == 0:
            return max(nums)
        return g

s = Solution()
print(s.maxSubArray([-2,-3]))


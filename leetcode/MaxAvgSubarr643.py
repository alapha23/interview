
class Solution:
    # sliding window
    def findMaxAverage(self, nums, k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]

        max_s = s
        for i in range(len(nums)-k):
            s -= nums[i]
            s += nums[i+k]
            if s > max_s:
                max_s = s
        return max_s/k

    # iteration O(N^2) Time Limit Exceeded
    def findMaxAverage2(self, nums, k: int) -> float:
        max_s = -10000 * k
        for i in range(len(nums)-k+1):
            s = 0
            for j in range(i, i+k):
                s += nums[j]
            if s > max_s:
                max_s = s

        return max_s/k


s = Solution()
print(s.findMaxAverage2([1,12,-5,-6,50,3],4))
print(s.findMaxAverage2([5],1))

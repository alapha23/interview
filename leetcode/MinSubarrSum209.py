class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        L = len(nums)+1
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s >= target:
                if (i+1) < L:
                    L = i+1
                    break
                    #print(s, i, L)
        if L == len(nums)+1:
            return 0
        # sliding window
        windowL = L
        right = L-1
        left = 0
        print(nums)
        while right < len(nums) and left < len(nums):
            #print(left, right,s)
            s -= nums[left]
            windowL -= 1
            left += 1
            if s >= target:
                L = windowL
                continue
            if right < len(nums) -1:
              s += nums[right+1]
              windowL += 1
              L  = windowL
              right += 1
        
        return L

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))

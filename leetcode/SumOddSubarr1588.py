class Solution:
    def sumOddLengthSubarrays(self, arr: list) -> int:
        # sum of all possible odd-length subarray
        result = 0
        rounds = (len(arr) // 2 + 1)
        # rounds = 3 -> window size 1, 3, 5
        if len(arr) % 2 == 0:
            rounds -= 1
        for i in range(rounds):
            l = i*2 + 1
            s = 0
            # initial window
            for k in range(l):
                s += arr[k]
            result += s
            #slide
            for j in range(1, len(arr)-l+1):
                s -= arr[j-1]
                s += arr[j+l-1]
                result += s

        return result

s = Solution()
print(s.sumOddLengthSubarrays([1,4]))

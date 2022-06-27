
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        kbty = 0

        for i in range(len(s) - k + 1):
            divisor = int(s[i:i+k])
            if divisor == 0:
                continue
            if num % divisor == 0:
                kbty += 1
        return kbty

s = Solution()
print(s.divisorSubstrings(240, 2))

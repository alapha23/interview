
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [0]*(m+n)
        x = 0
        y = 0
        idx = 0
        while x < m and y < n:
            print('looping',end='...')
            print(result)
            if nums1[x] > nums2[y]:
                result[idx] = nums2[y]
                y += 1
                idx += 1
            else:
                result[idx] = nums1[x]
                x += 1
                idx += 1
        if x == m:
            while y < n:
                print(result)
                result[idx] = nums2[y]
                idx += 1
                y += 1
        elif y == n:
            while x < m:
                print(result)
                result[idx] = nums1[x]
                idx += 1
                x += 1
        for i in range(m+n):
            nums1[i] = result[i]

s = Solution()
num1 = [2,0]
s.merge(num1, 1, [1],1)
print(num1)

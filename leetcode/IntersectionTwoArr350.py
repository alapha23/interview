
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        d1 = {}
        d2 = {}
        results = []
        for i in range(len(nums1)):
            if nums1[i] in d1:
                d1[nums1[i]] += 1
            else:
                d1[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] in d2:
                d2[nums2[i]] += 1
            else:
                d2[nums2[i]] = 1
 
        for i in range(len(nums2)):
            if nums2[i] in d1:
                results.append(nums2[i])
        l = len(results)
        i = 0
        while i < l:
            if results.count(results[i]) > min(d1[results[i]], d2[results[i]]):
                del results[i]
                l -= 1
                continue
            i += 1
        return results

s = Solution()
print(s.intersect([4,9,5], [9,4,9,8,4]))

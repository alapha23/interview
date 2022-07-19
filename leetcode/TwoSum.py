
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]][0] += 1
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [1, i] # count, index

        for i in range(len(nums)):
            n = nums[i]
            j = target - n
            if j in d:
                for k in range(1, len(d[j])):
                    if d[j][k] == i:
                        continue
                    else:
                        return [i, d[j][k]]

s = Solution()
#print(s.twoSum([3,2,4],6))
#print(s.twoSum([0,4,3,0],0))
print(s.twoSum([-1,-2,-3,-4,-5], -8))

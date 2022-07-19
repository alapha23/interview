
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        v = {}
        for n in nums:
            if n in v:
                return True
            v[n] = 1
        return False

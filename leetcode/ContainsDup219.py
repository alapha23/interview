
class Solution:
    # hashmap
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)

        for key in dic.keys():
            for i in range(len(dic[key])-1):
                if dic[key][i+1] - dic[key][i] <= k:
                    return True
        return False
    # sliding window size of min(k, len(nums))
    def containsNearbyDuplicate2(self, nums, k: int) -> bool:
        l = set()
        for i in range(len(nums)):
            if len(l) >= k+1:
                l.remove(nums[i-k-1]) # remove left-most elem
            if nums[i] in l:
                return True
            l.add(nums[i])
        return False
            
 

s = Solution()
print(s.containsNearbyDuplicate2([1,2,3,1],4))
print(s.containsNearbyDuplicate2([1,2,3,1,2,3],2))
#print(s.containsNearbyDuplicate2([1],1))
#print(s.containsNearbyDuplicate2([1,2],2))
#print(s.containsNearbyDuplicate2([1,0,1,1],1))

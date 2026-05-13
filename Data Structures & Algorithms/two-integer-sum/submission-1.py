class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            j = target - nums[i] 
            if j in hashmap.keys():
                return sorted([i, hashmap[j] ])
            else:
                hashmap[nums[i]] = i

            
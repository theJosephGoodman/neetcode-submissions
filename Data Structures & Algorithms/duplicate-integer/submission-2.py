class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap.get(i, 0) >= 2:
                return True
            

        return False
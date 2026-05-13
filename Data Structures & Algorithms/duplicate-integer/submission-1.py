class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hashmap = set()
        for i in range(len(nums)):
            if nums[i] in my_hashmap:
                return True
            my_hashmap.add(nums[i])
        return False
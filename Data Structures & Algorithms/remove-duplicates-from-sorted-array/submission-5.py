class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        memory = set()
        i = 0 
        valid_i = 0
        for i in range(len(nums)):
            if nums[i] not in memory:
                memory.add(nums[i])
                nums[valid_i] = nums[i]
                valid_i = valid_i + 1

        return len(memory)
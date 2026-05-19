class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()

        for num in nums:
            if num not in memory:
                memory.add(num)
            else:
                return True

        return False
        
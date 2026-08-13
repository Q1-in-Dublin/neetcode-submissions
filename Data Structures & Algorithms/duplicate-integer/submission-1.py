class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #just check it with length

        return len(nums) != len(set(nums))
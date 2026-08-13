class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Using ordering

        nums.sort()
        # ordering and if i and i+1 (near number is the same)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] :
                return True
        return False
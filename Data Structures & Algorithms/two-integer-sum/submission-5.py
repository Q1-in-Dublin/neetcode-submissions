class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find differ
        # get differ's index
        # sorting
        have_seen = {}

        for key,value in enumerate(nums):

            differ = target - value

            if differ in have_seen :
                return [have_seen[differ],key]
            have_seen[value] = key
        return []
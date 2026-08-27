
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # array string
        # way1 O(n)
        # iterate append.get(i,0) +1
        num_set = set()

        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)

        
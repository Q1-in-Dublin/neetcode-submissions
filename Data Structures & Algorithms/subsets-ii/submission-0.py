class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # order is not important
        # always include []
        n = len(nums)
        nums.sort()
        result = []
        def backtracking(index,current_path):
            result.append(list(current_path))
            for i in range(index,n):

                if i > index and nums[i] == nums[i-1]:
                    continue

                current_path.append(nums[i])

                backtracking(i+1, current_path)

                current_path.pop()



        backtracking(0,[])
        return result
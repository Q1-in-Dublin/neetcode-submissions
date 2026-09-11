class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #subset
        #not duplicated
        #all possible subset of nums => 2^n

        result = []
        path = []
        n = len(nums)
        def backtracking(index):
            
            if index == n:
                result.append(path[:])
                return
            backtracking(index+1)

            path.append(nums[index])
            backtracking(index+1)
            path.pop()
            return
                
        backtracking(0)
        return result


        

        

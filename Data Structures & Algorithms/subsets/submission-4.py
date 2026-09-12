class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #subset
        #not duplicated
        #all possible subset of nums => 2^n
        
        # Backtracking is extension of DFS
        # explore Choose , Explore, Check contraints, un-choose

        result = []
        n = len(nums)

        def backtracking(index,current_path):
            result.append(list(current_path))

            for i in range(index, n):
                current_path.append(nums[i])
                backtracking(i+1, current_path)
                current_path.pop()
                
        backtracking(0,[])
        return result
        

        

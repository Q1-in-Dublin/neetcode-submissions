class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # unique integers
        # all possible permutations
        # the other one is Combinations qustions => order is not a big deal
        # input same
        # ouput Permutation.. elements order is important
        # visited
        #base case?
        # len(nums) = current_path
        n = len(nums)
        result = []
        visited = [False] * n 

        def backtracking(current_path,visited):
            if len(current_path) == n :
                result.append(list(current_path))
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                # choose
                visited[i] = True
                current_path.append(nums[i])
                # explore
                backtracking(current_path,visited)
                # unchoose
                current_path.pop()
                visited[i] = False



        backtracking([],visited)
        return result
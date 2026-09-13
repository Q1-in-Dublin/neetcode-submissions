class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # unique integers
        # all possible permutations
        # input same
        # ouput Permutation.. elements order is important
        # any order
        # visited

        #base case?
        # len(nums) = current_path

        result = []
        n = len(nums)
        visited = [False] * n  

        def backtracking(current_path,visited):
            if len(current_path) == n :
                result.append(list(current_path))
                return

            for i in range(n):
                if visited[i] :
                    continue
                #change to visited
                visited[i] = True
                current_path.append(nums[i])

                #explore
                backtracking(current_path,visited)

                #unchoose
                current_path.pop()
                visited[i] = False


        backtracking([],visited)
        return result
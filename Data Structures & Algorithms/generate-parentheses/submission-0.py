class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n means the n pairs of parentheses
        # permutaion or Combinations
        # Order is important so permutation
        #State management : next step n * 2
        
        open_count = 0
        close_count = 0
        result = []


        def backtracking(open_count,close_count,current_path):
            if open_count == n and close_count == n :
                result.append("".join(current_path))
                return 
            
            
            if open_count < n :
                current_path.append("(")
                backtracking(open_count+1,close_count, current_path)
                current_path.pop()

            if close_count < open_count:
                current_path.append(")")
                backtracking(open_count,close_count+1, current_path)
                current_path.pop()


        backtracking(open_count,close_count,[])

        return result
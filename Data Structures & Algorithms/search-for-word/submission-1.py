class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #backtracking
        # 

        rows,cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c,word_index):
            #base case completed 
            if word_index == len(word):
                return True

            if(r < 0 or r>=rows or
             c<0 or c>= cols or
            board[r][c] != word[word_index]or
             (r,c) in visited): 
                return False
            
            #choose
            visited.add((r,c))

            # backtrack
            # if we can find it any direction then it's true
            res = (
                dfs(r-1,c,word_index+1)
                or dfs(r+1,c,word_index+1) 
                or dfs(r,c-1,word_index+1)
                or dfs(r,c+1,word_index+1)
            ) 
            # unchoose
            visited.remove((r,c))
            
            return res
            

            
            return False 

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False
        
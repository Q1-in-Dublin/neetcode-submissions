class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows,cols = len(board), len(board[0])
        visited = set()


        def dfs(r,c,word_index):
            # find it? base case 
            if word_index == len(word):
                return True

            #check the border exceed
            if (
                r < 0 
                or r>=rows
                or c<0
                or c >= cols 
                or board[r][c] != word[word_index]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            res = (dfs(r-1,c,word_index+1) or
            dfs(r+1,c, word_index+1) or
            dfs(r,c-1,word_index+1) or
            dfs(r,c+1,word_index+1))


            board[r][c] = temp

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False

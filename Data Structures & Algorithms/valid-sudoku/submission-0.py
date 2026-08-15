class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #9x9
        # no duplicate set
        #ignore "."
        # row, column and 9 cells
        #board에서 board[i][j] is 
        #board에서 borad[i][j]

        seen = set()
        for i in range(9) :
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                row_key = (i,val)
                col_key = (val,j)
                box_key = (i//3,j//3,val)

                if row_key in seen or col_key in seen or box_key in seen:
                
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True

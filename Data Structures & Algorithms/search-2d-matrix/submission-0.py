class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        # matrix = [[1,2,4,8], [i][j] row col
        #           [10,11,12,13],
        #           [14,20,30,40]]
        #           row ? len(matrix)
        #           col ? len(matrix[0])
        # tip is sorted already
        # constraint : Can you write a solution that runs in O(log(m * n)) time?

        rows, cols = len(matrix), len(matrix[0])
        # print(rows,cols)
        # need to iterate
        # output : T/F
        left,right = 0, rows*cols -1

        while left <= right :
            #keep iterate; same as binary search
            mid = (left + right) //2
            row,col = mid // cols, mid % cols
            val = matrix[row][col]

            if val == target :
                return True
            elif val < target:
                left = mid +1
            else:
                right = mid-1

        return False


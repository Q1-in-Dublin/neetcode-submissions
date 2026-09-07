class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        count = 1
        seen = set()

        def dfs(i,j):
            if (i<0 or i>=len(grid)) or (j<0 or j>=len(grid[0])) or (i,j) in seen or grid[i][j] == 0 :
                return 0
            seen.add((i,j))
            
            
            return 1 +dfs(i,j-1) + dfs(i,j+1)+ dfs(i-1,j) +dfs(i+1,j)




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j)
                    max_area =  max(max_area,area)
                        

        return max_area
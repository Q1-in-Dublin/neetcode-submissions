from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #nearest treasure chest => BFS(shortest route)
        # each treasure chest is the
        #-1 water , 0 treasure chest, inf - land cell 
        # inf => not need to make seen
        
        #destinaion
        rows,cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        print(queue)
        
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        while queue:
            #fifo
            r, c = queue.popleft()

            for dr, dc in directions:
                nr,nc = dr+r , dc+c

                #check is it not water? in the boundary Still INF?
                if (0 <= nr <rows and 0<=nc<cols and grid[nr][nc] == INF):
                    grid[nr][nc] = grid[r][c] +1 
                    queue.append((nr,nc))








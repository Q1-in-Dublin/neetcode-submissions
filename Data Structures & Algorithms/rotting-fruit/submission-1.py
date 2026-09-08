from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # minimum numter of minutes : BFS
        #inptu grid
        #output mini mins
        # no time -1

        queue = deque()
        time = 0
        fresh_count = 0
        directions = [(-1,0),(1,0), (0,-1), (0,1) ]
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        #time limit
        while queue:
            rotted_this_round = False   
            # len(queue) time limit
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr , nc = dr+ r, dc+ c

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # rotten
                        fresh_count -= 1
                        queue.append((nr,nc))
                        rotted_this_round =True 
            if rotted_this_round:  
                time+= 1
        
        return time if fresh_count ==0 else -1
        


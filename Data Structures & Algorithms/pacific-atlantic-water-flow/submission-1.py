class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # four direectin

        if not heights or not heights[0]:
            return []

        rows,cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs (r, c, reachable, prev_height):
            if (
                r < 0 or
                r >= rows or
                c < 0 or
                c >= cols or
                (r,c) in reachable or
                heights[r][c] < prev_height
            ):
                return


            reachable.add((r,c))
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r+dr, c+dc, reachable,heights[r][c])

        for c in range(cols):
            dfs(0,c, pacific_reachable, heights[0][c])
            dfs(
                rows-1, c, atlantic_reachable, heights[rows-1][c]
            )

        for r in range(rows):
            dfs(r,0, pacific_reachable, heights[r][0])
            dfs(
                r, cols-1, atlantic_reachable, heights[r][cols-1]
            )

        result = []
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):

                if (r,c) in pacific_reachable and (r,c) in atlantic_reachable:
                    result.append([r,c])
        return result
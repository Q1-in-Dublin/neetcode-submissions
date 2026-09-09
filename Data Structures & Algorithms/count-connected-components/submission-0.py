from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # how many connected edges it has
        # ex1 => 2 groups
        # ex2 => 1 group

        adj = {i : [] for i in range(n)}
        
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        count = 0
        
        visited = set()
        queue = deque()

        # check all nodes
        for i in range(n):
                if i not in visited:
                    count +=1
                
                # node i start bfs
                # fill in visited
                queue = deque([i])
                visited.add(i)
                
                while queue :
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return count




        
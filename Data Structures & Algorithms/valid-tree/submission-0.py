from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n seems like the number of nodes
        # list of undirected , could be circular? no circular
        # output t/f
        # what is valid tree?
        # Tree => no circular ,every node should be connected
        # n 개 node's edge is always n-1 
        visited = set([0]) #start node
        queue = deque([0])
        if len(edges) != n-1:
            return False

        adj = {i : [] for i in range(n)}
        #print(adj)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if neighbor not in visited :
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == n

        
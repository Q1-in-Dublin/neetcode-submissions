from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n seems like the number of nodes
        # list of undirected , could be circular? no circular
        # output t/f
        # what is valid tree?
        # Tree => no circular ,every node should be connected
        # n 개 node's edge is always n-1 
        if len(edges) != n-1:
            return False
        # n = 5
        #{0: [], 1: [], 2: [], 3: [], 4: []}
        adj = {i: [] for i in range(n)}
        #print(adj)

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}

        #print(adj)
        visited = set([0])
        queue = deque([0])

        while queue :
            #consumming que and adding
            next_node = queue.popleft()

            for neighbor in adj[next_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return len(visited) == n



        #time complexity : O(N+E) => O(n)
        # space : adj v, u  , Visited , queue
        #O(V+E)

        
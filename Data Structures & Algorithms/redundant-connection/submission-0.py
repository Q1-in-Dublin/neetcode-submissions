class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #undirected graph conencted each other
        #union find 
        # node n , edge n-1.. but one more edge .. what is not necessary edge
        # if the multiple answer , answer the last pair
        
        #find root
        #union combine node x and node y 's group

        n = len(edges)
        parent = [i for i in range(n+1)]
        #[0, 1, 2, 3, 4] ; 0 is dummy
        print(parent)

        def find(x):
            # root itself, return 
            if parent[x] == x:
                return x
            # find root node and update parent
            parent[x]= find(parent[x])
            return parent[x]

        def union(x,y):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False

            parent[root_u] = root_v
            return True
        #traverse edges and submit cycle finding edge
        for u, v in edges:
            if not union(u,v):
                return [u,v]
        
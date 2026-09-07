"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # input node
        # output node
        # deep copy : original vs copied different entity
        # non directed : 1->2 2->1, cycle .. 
        # one node no neighbour [[]]
        # no graph

        if not node:
            return None

        old_to_new = {}
        
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            new_node = Node(node.val)
            old_to_new[node] = new_node # new_node register

            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            return new_node

    
        return  dfs(node)
        
        

        
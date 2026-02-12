from typing import Optional
from collections import deque

class Node:
    def __init__(self,val = 0,neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph(adjList: list[list[int]]) -> Optional[Node]:
    if not adjList:
        return None
    
    # Create all nodes (1-indexed)
    nodes = {i + 1: Node(i + 1) for i in range(len(adjList))}
    
    # Assign neighbors
    for i, neighbors in enumerate(adjList):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    
    return nodes[1]  # first node (val = 1)

def graphToAdjList(node: Optional[Node]) -> list[list[int]]:
    if not node:
        return []

    adj = {}
    visited = set()
    queue = deque([node])
    visited.add(node)

    while queue:
        cur = queue.popleft()
        adj[cur.val] = []

        for nei in cur.neighbors:
            adj[cur.val].append(nei.val)
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

    # Return adjacency list in sorted order (LeetCode format)
    return [sorted(adj[i]) for i in sorted(adj)]


def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    
    start = node
    o_to_n = {}
    stk = [start]
    visited = set()
    visited.add(start)

    while stk:
        node = stk.pop()
        o_to_n[node] = Node(val = node.val)

        for nei in node.neighbors:
            if nei not in visited: 
                visited.add(nei)
                stk.append(nei)
        
    for old_nei, new_nei in o_to_n.items():
        for nei in old_nei.neighbors:
            nei_node = o_to_n[nei]
            new_nei.neighbors.append(nei_node)
    
    return o_to_n[start]


adjList1 = [[2,4],[1,3],[2,4],[1,3]]

original1 = buildGraph(adjList1)
cloned1 = cloneGraph(original1)
output1 = graphToAdjList(cloned1)

print("Input: ", adjList1)
print("Output:", output1)

adjList2 = [[]]
original2 = buildGraph(adjList2)
cloned2 = cloneGraph(original2)
output2 = graphToAdjList(cloned2)

print("Input: ", adjList2)
print("Output:", output2)

adjList3 = []
original3 = buildGraph(adjList3)
cloned3 = cloneGraph(original3)
output3 = graphToAdjList(cloned3)

print("Input: ", adjList3)
print("Output:", output3)


# Time O(E + V) Space O(V)
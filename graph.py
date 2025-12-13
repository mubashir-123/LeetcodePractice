# Array of Edges (Directed) [start,End]
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

# convert Array of Edges -> Adjacency List
from collections import defaultdict

D = defaultdict(list)

for u,v in A:
    D[u].append(v)

# print(D)    

# dfs recursive approach Time and Space: O(V + E)
def dfs_recursive(node):
    print("DFS recursive",node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)
dfs_recursive(source)

print()

def dfs_iterative(node):
    while stack: 
     node = stack.pop()
     print("DFS Iterative ",node) 
     for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node) 

source = 0
seen = set()
seen.add(source)
stack = [source]
dfs_iterative(stack)            

print()

# BFS (Queue) O(V + E)
from collections import deque

def bfs(node):
 while q:
     node = q.popleft()
     print("BFS: ",node)
     for nei_node in D[node]:
        if nei_node not in seen:
           seen.add(nei_node)
           q.append(nei_node)

source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)
bfs(q)

# defining the class

class Node:
   def __init__(self,value):
      self.value = value
      self.neighbors = []

   def __str__(self):
      return f'Node({self.value})' 

   def display(self):
      connections = [node.value for node in self.neighbors]
      return f'{self.value} is connected to {connections}'

A = Node('A')                    
B = Node('B')                    
C = Node('C')                    
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)
C.neighbors.append(D)
D.neighbors.append(C)

print(A.display())
print(B.display())
print(C.display())
print(D.display())

      
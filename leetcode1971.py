from collections import defaultdict,deque

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # 1. DFS with Recursive
    
    # if source == destination:
    #     return True
    
    # graph = defaultdict(list)
    
    # for u,v in edges:
    #     graph[u].append(v)
    #     graph[v].append(u)
    
    # seen = set()
    # seen.add(source)

    # def dfs(i):
    #     if i == destination:
    #         return True
        
    #     for nei_node in graph[i]:
    #         if nei_node not in seen:
    #             seen.add(nei_node)
    #             if dfs(nei_node):
    #                 return True
    #     return False
    # return dfs(source)

    # 2. DFS with Stack (iterative)
    
    # if source == destination:
    #     return True
    
    # graph = defaultdict(list)
    
    # for u,v in edges:
    #     graph[u].append(v)
    #     graph[v].append(u)
    
    # seen = set()
    # seen.add(source)
    # stack = [source]

    # while stack:
    #     node = stack.pop()
    #     if node == destination:
    #         return True
    #     for nei_node in graph[node]:
    #         if nei_node not in seen:
    #             seen.add(nei_node)
    #             stack.append(nei_node) 
    # return False

    # 3. BFS with Deque
    if source == destination:
        return True
    
    graph = defaultdict(list)
    
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    seen = set()
    seen.add(source)
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)
    return False

# graph 1
n1 = 3
edges1 = [[0,1],[1,2],[2,0]]
source1 = 0
destination1 = 2

# graph 2
n2 = 6
edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source2 = 0
destination2 = 5

print("Graph 1: ",validPath(n1,edges1,source1,destination1))
print("Graph 2: ",validPath(n2,edges2,source2,destination2))

# Time O(N + E) Space O(N + E)

from collections import defaultdict

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    g = defaultdict(list)
    courses = prerequisites

    for a,b in courses:
        g[a].append(b)
    
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    states = [UNVISITED] * numCourses

    def dfs(node):
        state = states[node]
        if state == VISITED:
            return True
        elif state == VISITING:
            return False
        
        states[node] = VISITING

        for nei in g[node]:
            if not dfs(nei):
                return False
            
        states[node] = VISITED
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True

# Graph 1
numCourses1 = 2
prerequisites1 = [[1,0]]
print(canFinish(numCourses1,prerequisites1))

# Graph 2
numCourses2 = 2
prerequisites2 = [[1,0],[0,1]]
print(canFinish(numCourses2,prerequisites2))

# Time O(N + E) Space O(N + E)
from collections import defaultdict

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    order = []
    g = defaultdict(list)
    for a,b in prerequisites:
        g[b].append(a)
    
    UNVISITED, VISITING ,VISITED = 0, 1, 2

    states = [UNVISITED] * numCourses

    # Detecting cycle if true else no cycle false 
    def dfs(i):
        if states[i] == VISITING:
            return False
        elif states[i] == VISITED:
            return True
        
        states[i] = VISITING

        for nei in g[i]:
            if not dfs(nei):
                return False
            
        states[i] = VISITED
        order.append(i)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []
    
    return order

numCourses1 = 2
prerequisites1 = [[1,0]]
print(findOrder(numCourses1,prerequisites1))

numCourses2 = 4
prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses2,prerequisites2))

numCourses3 = 1
prerequisites3 = []
print(findOrder(numCourses3,prerequisites3))

# Time O(V + E) Space O(V + E)
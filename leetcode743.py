import heapq
from collections import deque, defaultdict

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u,v,time in times:
        graph[u].append((v,time))
    
    min_times = {}
    min_heap = [(0,k)]

    while min_heap:
        d,i = heapq.heappop(min_heap)
        if i in min_heap:
            continue
        
        min_times[i] = d
        for nei,nei_time in graph[i]:
            if nei not in min_times:
                heapq.heappush(min_heap,(d + nei_time,nei))
    
    if len(min_times) == n:
        return max(min_times.values())
    else:
        return -1


times1 = [[2,1,1],[2,3,1],[3,4,1]]
n1= 4
k1 = 2

times2 = [[1,2,1]]
n2 = 2
k2 = 1

times3 = [[1,2,1]]
n3 = 2
k3 = 2

# Time O((V + E) log(V))
# Space O(V + E)

print("Minimum time 1: ",networkDelayTime(times1,n1,k1))
print("Minimum time 2: ",networkDelayTime(times2,n2,k2))
print("Minimum time 3: ",networkDelayTime(times3,n3,k3))
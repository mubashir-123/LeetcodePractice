intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[4,7],[1,4]]

def mergeInterval(intervals: list[list[int]]) -> list[list[int]] :
    intervals.sort(key = lambda interval: interval[0])
    merge = []

    for interval in intervals:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1] = merge[-1][0],max(merge[-1][1],interval[1])
    return merge

print(mergeInterval(intervals1))
print()    
print(mergeInterval(intervals2))    

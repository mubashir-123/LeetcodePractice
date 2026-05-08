
def hIndex(citations: list[int]) -> int:
    n = len(citations)
    paper_count = [0] * (n + 1)

    for c in citations:
        paper_count[min(n,c)] += 1
    
    h = n
    paper = paper_count[n]

    while paper < h:
        h -= 1
        paper += paper_count[h]
    
    return h

citations1 = [3,0,6,1,5]
print(hIndex(citations1))

citations2 = [1,3,1]
print(hIndex(citations2))

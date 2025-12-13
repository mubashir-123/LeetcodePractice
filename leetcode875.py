from math import ceil
piles1 = [3,6,7,11]
h1 = 8

piles2 = [30,11,23,4,20]
h2 = 5

piles3 = [30,11,23,4,20]
h3 = 6

def minEatingBananas(piles: list[int],h: int) -> int:
    def k_hour(k):
        hours = 0
        for p in piles:
            hours += ceil(p/k)
        return hours <= h
    
    l = 1
    r = max(piles)

    while l < r:
        k = l + (r - l) // 2
        if k_hour(k):
            r = k
        else:
            l = k + 1
    return l

print(minEatingBananas(piles1,h1))
print(minEatingBananas(piles2,h2))
print(minEatingBananas(piles3,h3))

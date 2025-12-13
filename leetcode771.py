jewels1 = "aA" 
stones1 = "aAAbbbb"
jewels2 = "z" 
stones2 = "ZZ"

def numJewelInStones(jewel: str,stones: str) -> int:
    count = 0
    s = set(jewel)

    for stone in stones:
        if stone in s:
            count += 1
    return count

print(numJewelInStones(jewels1,stones1))           
print(numJewelInStones(jewels2,stones2))           

# Time O(n + m) (due to use of set) Space O(n) 

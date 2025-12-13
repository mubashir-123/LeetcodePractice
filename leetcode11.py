height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]

# Time O(n)
# Space O(1)

def maxCount(height: list[int]) -> int:
    n = len(height)
    l = 0
    r = n - 1
    max_count = 0

    while l < r:
        w = r - l
        h = min(height[l],height[r])
        a = w * h
        max_count = max(max_count,a)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_count

print(maxCount(height1))
print(maxCount(height2))
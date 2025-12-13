height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]

# Time O(n)
# Time O(n)

def trap(height: list[int]) -> int:
    n = len(height)
    l_wall = 0
    r_wall = 0
    left_max = [0] * n
    right_max = [0] * n

    for i in range(n):
        j = -i - 1
        left_max[i] = l_wall
        right_max[j] = r_wall
        l_wall = max(l_wall,height[i])
        r_wall = max(r_wall,height[j])
    
    summ = 0
    for i in range(n):
        pot = min(left_max[i],right_max[i])
        summ += max(0,pot - height[i])
    return summ

print(trap(height1))
print(trap(height2))

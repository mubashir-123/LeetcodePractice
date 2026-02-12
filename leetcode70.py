
def climbStairs(n: int) -> int:
    # Using Fabinacci series
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    prev, curr = 1, 2

    for i in range(2,n):
        prev, curr = curr, prev + curr
    
    return curr

n1 = 2
n2 = 3

print(climbStairs(n1))
print(climbStairs(n2))

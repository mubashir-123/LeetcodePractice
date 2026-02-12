
def fib(n: int) -> int:
    #Approach use Botton to Up and memoization
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    prev, curr = 0, 1

    for i in range(2,n + 1):
        prev, curr = curr, prev + curr
    
    return curr

n1 = 2
n2 = 3
n3 = 4

# Time O(n) Space O(1)

print(fib(n1))
print(fib(n2))
print(fib(n3))
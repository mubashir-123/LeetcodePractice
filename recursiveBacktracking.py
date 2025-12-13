class recursiveBacktracking:
    def subets(self,nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res,sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Dont Pick number
            backtrack(i+1)

            #Pick numbers
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)    
        res.sort(key = lambda x: (len(x),x))
        return res 
            

obj = recursiveBacktracking()
nums = [1,2,3]
result = obj.subets(nums)
print(result)


#  Dynamic Programming

class fibonacci:
    # Naive Recurssive approach Time complexity O(2^n)
    def naive(self,n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.naive(n - 2) + self.naive(n - 1)
    
    def top_down_memoization(self,n: int) -> int:
        memo = {0:0 , 1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x - 2)
                return memo[x]
        return f(n)    

obj = fibonacci()
n = 4
print("----------- Fibonacci-------------")
print(obj.naive(n))
print(obj.top_down_memoization(n))
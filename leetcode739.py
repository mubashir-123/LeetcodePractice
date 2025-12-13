temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]

# Time O(n)
# Space O(n)

def dailyTemperature(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stk = []
    answer = [0] * n

    for i,t in enumerate(temperatures):
        while stk and stk[-1][0] < t:
            stk_t,stk_i = stk.pop()
            answer[stk_i] = i - stk_i

        stk.append((t,i))
    return answer

print(dailyTemperature(temperatures1)) 
print(dailyTemperature(temperatures2)) 
print(dailyTemperature(temperatures3)) 
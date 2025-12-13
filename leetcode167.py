numbers1 = [2,7,11,15]
target1 = 9
numbers2 = [2,3,4]
target2 = 6
numbers3 = [-1,0]
target3 = -1

# Time O(n)
# space O(1)

def twoSum(numbers: list[int],target: list[int]) -> list[int]:
    n = len(numbers) 
    l = 0
    r = n - 1

    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1,r + 1]
        elif sum < target:
            l += 1
        else:
            r -= 1

print(twoSum(numbers1,target1))
print(twoSum(numbers2,target2))
print(twoSum(numbers3,target3))
# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

case1 = [-4,-2,1,4,8]
case2 = [2,-1,1]

def findClosestNumber(nums: list[int]) -> int:
    closest = nums[0]
    for x in nums:
        if abs(x) < abs(closest):
                closest = x
            
    if closest < 0 and abs(closest) in nums:
        return abs(closest)
            
    else:
        return closest
    
print(findClosestNumber(case1))    
print(findClosestNumber(case2))    


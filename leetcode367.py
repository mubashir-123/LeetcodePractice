num1 = 16
num2 = 14

def isPerfectSquare(num: int) -> bool:

    # <----------------- Newton Method ----------------->

    # x = num
    
    # while x * x > num:
    #     x = (x + num//x) // 2
    # return x * x == num

    # <---------------- Binary Method ----------------->
    l = 0
    r = num

    while l <= r:
        m = l + (r - l) // 2
        m_squared = m * m
        if num == m_squared:
            return True
        elif m_squared < num:
            l = m + 1
        else:
            r = m - 1
    return False 

print(isPerfectSquare(num1))
print(isPerfectSquare(num2))
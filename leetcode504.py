def convertToBase7(num: int) -> str:
    # Time and Space O(log_7(N))
    if num == 0:
        return '0'
    
    original_num = num
    num = abs(num)
    remainders = []

    while num > 0:
        remainder = num % 7
        remainders.append(str(remainder))
        num //= 7
    
    if original_num < 0:
        remainders.append('-')

    remainders.reverse()
    return ''.join(remainders)

num1 = 100
print(convertToBase7(num1))

num2 = -7
print(convertToBase7(num2))
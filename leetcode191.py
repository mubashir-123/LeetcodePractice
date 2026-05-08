
def hammingWeight(n: int) -> int:
    # Time 0(NumberOfOnes) Space 0(1)
    ans = 0

    while n != 0:
        ans += 1
        n = n & (n - 1)
    return ans

n1 = 11
print(hammingWeight(n1))

n2 = 128
print(hammingWeight(n2))

n3 = 2147483645
print(hammingWeight(n3))
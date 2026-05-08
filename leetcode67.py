
def addBinary(a: str, b: str) -> str:
    # Time O(A + B) Space O(1)
    a,b = int(a,2), int(b,2)

    while b:
        without_carry = a ^ b
        carry = (a & b) << 1
        a,b = without_carry, carry
    return bin(a)[2:]


a1 = "11"
b1 = "1"
print(addBinary(a1,b1))

a2 = "1010"
b2 = "1011"
print(addBinary(a2,b2))
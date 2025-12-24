s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"

def isValid(s: str) -> bool:
    # hashmap = {')':'(','}':'{',']':'['}
    # stk = []

    # for c in s:
    #     if c not in hashmap:
    #         stk.append(c)
    #     else:
    #         if not stk:
    #             return False
    #         else:
    #             popped = stk.pop()
    #             if popped != hashmap[c]:
    #                 return False
    
    # return not stk

    hashmap = {')': '(','}' : '{', ']' : '['}
    stk = []

    for c in s:
        if c not in hashmap:
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != hashmap[c]:
                    return False
    return not stk
                

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
print(isValid(s5))
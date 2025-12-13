from math import ceil, floor
tokens1 = ["2","1","+","3","*"]
tokens2= ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

# Time O(n)
# Space O(n)

def evalRPN(tokens: list[str]) -> int:
    stk = []

    for t in tokens:
        if t in '+-*/':
            b, a = stk.pop(), stk.pop()
            if t == '+':
                stk.append(a + b)
            elif t == '-':
                stk.append(a - b)
            elif t == '*':
                stk.append(a * b)
            else:
                division = a / b
                if division < 0:
                    stk.append(ceil(division))
                else:
                    stk.append(floor(division))
        else:
            stk.append(int(t))
    return stk[0]

print(evalRPN(tokens1))
print(evalRPN(tokens2))
print(evalRPN(tokens3))
from collections import deque

class Trees:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
def pre_order(node): # Recursive Pre_order traversal (DFS) Time: O(n) space: O(n)
    if not node:
        return
        
    print(node)
    pre_order(node.left)        
    pre_order(node.right)        

def in_order(node): # Recursive In_order traversal (DFS) Time: O(n) space: O(n)
    if not node: 
        return

    in_order(node.left)
    print(node)
    in_order(node.right)    

def pre_order_iteration(node): # Iterative Pre_order traversal (DFS) Time: O(n) space: O(n)
    if not node: 
        return
    
    stk = [node]
    
    while(stk):
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

def level_order(node): # level order iteration (BFS) Time: O(n) Space O(n)
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left : q.append(node.left)
        if node.right: q.append(node.right)

# check the va;ue if exist Time O(n) space O(n)    
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    
    return search(node.left,target) or search(node.right,target)

def binary_search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val: 
         return binary_search(node.left, target)
    else:
         return binary_search(node.right, target)    

A = Trees(5)
B = Trees(1)
C = Trees(8)
D = Trees(-1)
E = Trees(3)
F = Trees(7)
G = Trees(9)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

# print("Pre Order")
# pre_order(A)

# print("In Order")
# in_order(A)

# pre_order_iteration(A)

# level_order(A)

# print(search(A,-1))

# print(binary_search(A, 8))


# Traditional Binary Search - Looking up if number is in array
# Time O(logN)
# Space O(N)

def binary_search_traditional(arr,target):
    N = len(arr)
    L = 0
    R = N - 1

    while L <= R:
        M = L + ((R - L) // 2)

        if  target == arr[M] :
            return True 
        elif target < arr[M]  :
            R = M - 1
        else:
            L = M + 1
    
    return False

A = [-3, -1, 0, 1, 4, 7]

print(binary_search_traditional(A, 0))

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = L + ((R - L)//2)

        if arr[M]:
            R = M
        else:
            L = M + 1    
    return L

B = [False,False,False,True,True,True,True]
print(binary_search_condition(B))
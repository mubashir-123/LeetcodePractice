from collections import deque
from typing import Optional

class TreeNode:
    # Defining the TreeNode class again for completeness
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    """
    Performs a Level-Order Traversal (BFS) using a Queue.
    Returns a list of node values.
    """
    if not root:
        return []
        
    # Initialize a queue and a result list
    queue = deque([root])
    result = []
    
    while queue:
        # 1. Dequeue the node at the front (visiting the current node)
        node = queue.popleft()
        result.append(node.val)
        
        # 2. Enqueue the left child if it exists
        if node.left:
            queue.append(node.left)
            
        # 3. Enqueue the right child if it exists
        if node.right:
            queue.append(node.right)
            
    return result

class Solution:
    def isSameTree(self,p: Optional[TreeNode],q: Optional[TreeNode]) -> bool:
    # Time O(n + m) Space O(h_p,h_q)
        # def balance(p,q):
        #     if not p and not q:
        #         return True
            
        #     if not p or not q:
        #         return False
            
        #     if p.val != q.val:
        #         return False
            
        #     return balance(p.left,q.left) and balance(p.right,q.right)
        
        # return balance(p,q)

        def balanced(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return balanced(p.left,q.left) and balanced(p.right,q.right)
        return balanced(p,q)

sol = Solution()

# Tree 1    
node11 = TreeNode(2)
node12 = TreeNode(3)
root11 = TreeNode(1,left = node11,right=node12)

node21 = TreeNode(2)
node22 = TreeNode(3)
root12 = TreeNode(1,left = node21,right=node22)

# Tree 2
node21 = TreeNode(2)
root21 = TreeNode(1,left=node21)

node22 = TreeNode(2)
root22 = TreeNode(1,right=node22)

# Tree3
node31 = TreeNode(1)
node32 = TreeNode(2)
root31 = TreeNode(1,left=node32,right=node31)

node33 = TreeNode(1)
node34 = TreeNode(2)
root32 = TreeNode(1,left=node33,right=node34)

p1 = levelOrderTraversal(root11)
print(f"The Level-Order Traversal array root1: {p1}")

q1 = levelOrderTraversal(root12)
print(f"The Level-Order Traversal array root1: {q1}")

print()
result1 = sol.isSameTree(root11,root12)
print(f"Is same Tree?: {result1}")

print()
p2 = levelOrderTraversal(root21)
print(f"The Level-Order Traversal array root1: {p2}")

q2 = levelOrderTraversal(root22)
print(f"The Level-Order Traversal array root1: {q2}")

print()
result2 = sol.isSameTree(root21,root22)
print(f"Is same Tree?: {result2}")

print()
p3 = levelOrderTraversal(root31)
print(f"The Level-Order Traversal array root1: {p3}")

q3 = levelOrderTraversal(root32)
print(f"The Level-Order Traversal array root1: {q3}")

print()
result3 = sol.isSameTree(root31,root32)
print(f"Is same Tree?: {result3}")


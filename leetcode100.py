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
        def balance(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return balance(p.left,q.left) and balance(p.right,q.right)
        
        return balance(p,q)
    
node11 = TreeNode(2)
node12 = TreeNode(3)
root1 = TreeNode(1,left = node11,right=node12)

node21 = TreeNode(2)
node22 = TreeNode(3)
root2 = TreeNode(1,left = node21,right=node22)

p = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {p}")

q = levelOrderTraversal(root2)
print(f"The Level-Order Traversal array root1: {q}")

sol = Solution()
result1 = sol.isSameTree(root1,root2)
print(f"Is same Tree?: {result1}")


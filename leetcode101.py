from collections import deque
from typing import Optional

class TreeNode:
    # Defining the TreeNode class again for completeness
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    if not root:
        return []
        
    # Initialize a queue and a result list
    queue = deque([root])
    result = []
    
    while queue:
        # 1. Dequeue the node at the front (visiting the current node)
        node = queue.popleft()
        result = result.append(node.val)
        
        # 2. Enqueue the left child if it exists
        if node.left:
            queue.append(node.left)
            
        # 3. Enqueue the right child if it exists
        if node.right:
            queue.append(node.right)
            
    return result

class Solution:
    def isSymmetric(self,root: Optional[TreeNode]) -> bool:
        # Time O(n) Space O(n)
        def same(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return same(root1.left,root2.right) and same(root1.right,root2.left)
        return same(root,root)

# Tree1
node11 = TreeNode(3)
node12 = TreeNode(4)

node13 = TreeNode(4)
node14 = TreeNode(3)

node15 = TreeNode(2,left=node11,right=node12)
node16 = TreeNode(2,left=node13,right=node14)

root1 = TreeNode(1,left=node15,right=node16)

#Tree2
node21 = TreeNode(3)
node22 = TreeNode(3)

node23 = TreeNode(2,right=node21)
node24 = TreeNode(2,right=node22)

root2 = TreeNode(1,left=node23,right=node24)

traversal_result1 = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {traversal_result1}")

traversal_result2 = levelOrderTraversal(root2)
print(f"The Level-Order Traversal array root1: {traversal_result2}")



isSame = Solution()
result1 = isSame.isSymmetric(root1)
result2 = isSame.isSymmetric(root2)
print("Is symmetric tree: ",result1)
print("Is symmetric tree: ",result2)

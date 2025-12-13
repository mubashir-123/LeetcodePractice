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

class Solution():
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left,right)

# root 1
node11 = TreeNode(0)
node31 = TreeNode(0)
node61 = TreeNode(15)
node91 = TreeNode(7)

# Intermediate nodes:
node21 = TreeNode(9, left=node11, right=node31) 
node71 = TreeNode(20, left=node61, right=node91)

# Root node:
root1 = TreeNode(3, left=node21, right=node71)

# Root 2
node13 = TreeNode(0)
node23 = TreeNode(2)

root2 = TreeNode(1,node13,node23)

traversal_result1 = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {traversal_result1}")

traversal_result2 = levelOrderTraversal(root2)
print(f"The Level-Order Traversal array root1: {traversal_result2}")

invertedNode = Solution() # This instance is now only used for maxDepth
depth_result1 = invertedNode.maxDepth(root1)
print(f"Max Depth of root1: {depth_result1}")

depth_result2 = invertedNode.maxDepth(root2)
print(f"Max Depth of root1: {depth_result2}")


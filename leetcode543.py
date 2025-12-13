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
    # Time O(n) Space O(h)
    def diameterOfBinaryTree(self,root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            max_diameter[0] = max(max_diameter[0],right+left)

            return 1 + max(left,right)
        
        height(root)
        return max_diameter[0]

# root 1
node11 = TreeNode(4)
node12 = TreeNode(5)

node13 = TreeNode(2,left = node11,right=node12)
node14 = TreeNode(3)

root1 = TreeNode(1,left = node13,right = node14)

traversal_result1 = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {traversal_result1}")

diameter = Solution()
diameter_Tree = diameter.diameterOfBinaryTree(root1)
print(f"Diameter of Tree: {diameter_Tree}")

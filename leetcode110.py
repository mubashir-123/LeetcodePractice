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
    # Time O(n) Space O(n)
    def isBlanaced(self,root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            
            if balanced[0] is False:
                return 0
             
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            return 1 + max(left_height,right_height)    
        
        height(root)
        return balanced[0]     

# root1
node11 = TreeNode(15)
node12 = TreeNode(7)

node13 = TreeNode(9)
node14 = TreeNode(20,left = node11,right = node12)

root1 = TreeNode(3,left = node13,right = node14)

traversal_result1 = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {traversal_result1}")

balancedNode = Solution()
is_balanced_result = balancedNode.isBlanaced(root1)
print(f"Is root1 balanced? {is_balanced_result}")
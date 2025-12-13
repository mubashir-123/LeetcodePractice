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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time O(n)  Space O(h)
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# --- 🌲 Constructing Your Tree ---

# We reuse the tree constructed earlier:
# Root: 4 -> Left: 2 (with 1, 3) and Right: 7 (with 6, 9)

# root 1
node11 = TreeNode(1)
node31 = TreeNode(3)
node61 = TreeNode(6)
node91 = TreeNode(9)

# Intermediate nodes:
node21 = TreeNode(2, left=node11, right=node31) 
node71 = TreeNode(7, left=node61, right=node91)

# Root node:
root1 = TreeNode(4, left=node21, right=node71)

# Root 2
node12 = TreeNode(1)
node32 = TreeNode(3)

root2 = TreeNode(2, left=node12, right=node32) 

# Root 3
root3 = TreeNode()


traversal_result = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {traversal_result}")
traversal_result = levelOrderTraversal(root2)
print(f"The Level-Order Traversal array root2: {traversal_result}")
traversal_result = levelOrderTraversal(root3)
print(f"The Level-Order Traversal array root3: {traversal_result}")

invertedNode = Solution()
print("Inverted Tree Level-Order root1:",levelOrderTraversal(invertedNode.invertTree(root1)))
print("Inverted Tree Level-Order root2:",levelOrderTraversal(invertedNode.invertTree(root2)))
print("Inverted Tree Level-Order root3:",levelOrderTraversal(invertedNode.invertTree(root3)))



from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    if not root:
        return []
        
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result 

class Solution:
    def hasPathSum(self,root: Optional[TreeNode], targetSum: int) -> bool:
        # Time O(n) # Space O(n) 
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        new_target = targetSum - root.val
        return (self.hasPathSum(root.left,new_target) or self.hasPathSum(root.right,new_target))
    
sol = Solution()

# Tree1
node11 = TreeNode(7)
node12 = TreeNode(2)
node13 = TreeNode(1)

node14 = TreeNode(11,left=node11,right=node12)
node15 = TreeNode(13)
node16 = TreeNode(4,right=node13)

node17 = TreeNode(4,left=node14)
node18 = TreeNode(8,left=node15,right=node16)

root1 = TreeNode(5,left=node17,right=node18)

traverse_result1 = levelOrderTraversal(root1)
print("Tree 1: ",traverse_result1) 

result1 = sol.hasPathSum(root1,22)
print("Has Path Sum? ",result1)

# Tree 2
node21 = TreeNode(2)
node22 = TreeNode(3)
root2 = TreeNode(1,left=node21,right=node22)

traverse_result2 = levelOrderTraversal(root2)
print("Tree 2: ",traverse_result2) 

result2 = sol.hasPathSum(root2,5)
print("Has Path Sum? ",result2)

# Tree 3
root3 = TreeNode()
traverse_result3 = levelOrderTraversal(root3)
print("Tree 3: ",traverse_result3) 

result3 = sol.hasPathSum(root3,0)
print("Has Path Sum? ",result3)
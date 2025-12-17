from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            levels = []
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                levels.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(levels)

        return ans
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,minn,maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return isValid(node.left,minn,node.val) and isValid(node.right,node.val,maxx)
        return isValid(root,float('-inf'),float('inf'))

# Tree 1
node11 = TreeNode(1)
node12 = TreeNode(3)
root1 = TreeNode(2,left=node11,right=node12)

# Tree 2
node21 = TreeNode(3)
node22 = TreeNode(6)

node23 = TreeNode(1)
node24 = TreeNode(4,left=node21,right=node22)

root2 = TreeNode(5,left=node23,right=node24)

sol = Solution()
traverse_result2 = sol.levelOrder(root1)
print("Tree 1: ",traverse_result2)
validBST1 = sol.isValidBST(root1)
print("Is valid BST 1: ",validBST1)

traverse_result2 = sol.levelOrder(root2)
print("Tree 2: ",traverse_result2)
validBST2 = sol.isValidBST(root2)
print("Is valid BST 1: ",validBST2)
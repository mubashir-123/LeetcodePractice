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
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Time O(n) Spcae O(n) (We use Inorder traverse to traverse in sequence in ascending)
        prev = [None]
        md = [float('inf')]

        def dfs(node):
            if not node:
                return []
            
            dfs(node.left)

            if prev[0] is not None:
                md[0] = min(md[0],node.val - prev[0])
            
            prev[0] = node.val

        dfs(root)
        return md[0]

# Tree 1
node13 = TreeNode(1)
node14 = TreeNode(3)

node11 = TreeNode(2,left=node13,right=node14)
node12 = TreeNode(6)

root1 = TreeNode(4,left=node11,right=node12)

# Tree 2
node21 = TreeNode(12)
node22 = TreeNode(49)

node23 = TreeNode(0)
node24 = TreeNode(48,left=node21,right=node22)

root2 = TreeNode(1,left=node23,right=node24)

sol = Solution()
traverse_result1 = sol.levelOrder(root1)
print("Tree 1: ",traverse_result1)

minDiff1 = sol.getMinimumDifference(root1)
print("Minimum difference: ",minDiff1)

traverse_result2 = sol.levelOrder(root2)
print("Tree 1: ",traverse_result2)

minDiff2 = sol.getMinimumDifference(root2)
print("Minimum difference: ",minDiff2)

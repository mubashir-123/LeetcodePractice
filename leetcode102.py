from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time O(n) Space O(n)
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

node11 = TreeNode(15)    
node12 = TreeNode(7)

node13 = TreeNode(9)
node14 = TreeNode(20,left=node11,right=node12)

root1 = TreeNode(3,left=node13,right=node14)

root2 = TreeNode(1)
root3 = TreeNode()

sol = Solution()
traverse_result1 = sol.levelOrder(root1)
print("Level Order: ",traverse_result1)

traverse_result2 = sol.levelOrder(root2)
print("Level Order: ",traverse_result2)

traverse_result3 = sol.levelOrder(root3)
print("Level Order: ",traverse_result3)


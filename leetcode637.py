from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self,root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            avg = 0
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                avg += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            avg /= n
            ans.append(avg)
        
        return ans

# Tree 1
node11 = TreeNode(15)    
node12 = TreeNode(7)

node13 = TreeNode(9)
node14 = TreeNode(20,left=node11,right=node12)

root1 = TreeNode(3,left=node13,right=node14)

# Tree 2
node21 = TreeNode(15)
node22 = TreeNode(7)

node23 = TreeNode(9,left=node21,right=node22)
node24 = TreeNode(20)

root2 = TreeNode(3,left=node23,right=node24)

sol = Solution()
traver_result1 = sol.averageOfLevels(root1)
print("Tree 1 average node: ",traver_result1)

traver_result2 = sol.averageOfLevels(root2)
print("Tree 2 average node: ",traver_result2)


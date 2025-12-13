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
    
    def kthSmallest(self,root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            if count[0] == 1:
                ans[0] = node.val

            count[0] = count[0] - 1
            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return ans[0]  

 # Tree 1    
node11 = TreeNode(2)

node12 = TreeNode(1,right=node11) 
node13 = TreeNode(4) 

root1 = TreeNode(3,left=node12,right=node13)

# Tree 2
node21 = TreeNode(1)

node22 = TreeNode(2,left=node21)
node23 = TreeNode(4)

node24 = TreeNode(3,left=node22,right=node23)
node25 = TreeNode(6)

root2 = TreeNode(5,left=node24,right=node25)

sol = Solution()

tree1 = sol.levelOrder(root1)
print("Tree 1: ",tree1)
kth1 = sol.kthSmallest(root1,1)
print("Kth element: ",kth1)

tree2 = sol.levelOrder(root2)
print("Tree 2: ",tree2)
kth2 = sol.kthSmallest(root2,3)
print("Kth element: ",kth2)
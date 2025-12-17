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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root):
            if not root:
                return 
            
            lca[0] = root

            if root.val is p or root.val is q:
                return 
            elif root.val < p.val and root.val < q.val:
                return search(root.right)
            elif root.val > p.val and root.val > q.val:
                return search(root.left)
            else:
                return 
        search(root)
        return lca[0]

# Tree 1
node11 = TreeNode(3)
node12 = TreeNode(5)

node13 = TreeNode(0)
node14 = TreeNode(4,left=node11,right=node12)
node15 = TreeNode(7)
node16 = TreeNode(9)

node17 = TreeNode(2,left=node13,right=node14)
node18 = TreeNode(8,left=node15,right=node16)

root1 = TreeNode(6,left=node17,right=node18)
p1 = TreeNode(2)
q1 = TreeNode(8)

# Tree 2
node21 = TreeNode(3)
node22 = TreeNode(5)

node23 = TreeNode(0)
node24 = TreeNode(4,left=node21,right=node22)
node25 = TreeNode(7)
node26 = TreeNode(9)

node27 = TreeNode(2,left=node23,right=node24)
node28 = TreeNode(8,left=node25,right=node26)

root2 = TreeNode(6,left=node27,right=node28)
p2 = TreeNode(2)
q2 = TreeNode(4)

# Tree 3
node31 = TreeNode(1)
root3 = TreeNode(2,left=node31)
p3 = TreeNode(2)
q3 = TreeNode(1)

sol = Solution()
traverse_result1 = sol.levelOrder(root1) 
print("Tree 1: ",traverse_result1)
lca1 = sol.lowestCommonAncestor(root1,p1,q1)
print("LCA 1: ",lca1.val)

traverse_result2 = sol.levelOrder(root2) 
print("Tree 2: ",traverse_result2)
lca2 = sol.lowestCommonAncestor(root2,p2,q2)
print("LCA 2: ",lca2.val) 

traverse_result3 = sol.levelOrder(root3) 
print("Tree 3: ",traverse_result3)
lca3 = sol.lowestCommonAncestor(root3,p3,q3)
print("LCA 3: ",lca3.val) 
from collections import deque
from typing import Optional

class TreeNode:
    # Defining the TreeNode class again for completeness
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
    # Time O(n + m) and Space O(n)
    def isSubTree(self,root: Optional[TreeNode],subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False

            return same(p.left,q.left) and same(p.right,q.right)

        def hasTree(root,subRoot):
            if not root:
                return False

            if same(root,subRoot):
                return True
            
            return hasTree(root.left,subRoot) or hasTree(root.right,subRoot)
        
        return hasTree(root,subRoot)

# Tree 1
node11 = TreeNode(1) 
node12 = TreeNode(2)

node13 = TreeNode(4,left=node11,right=node12)
node14 = TreeNode(5)

root1 = TreeNode(3,left=node13,right=node14)

# subTree 1

sub_node11 = TreeNode(1)
sub_node12 = TreeNode(2)

sub_root = TreeNode(4,left=node11,right=node12)

traversal_result1 = levelOrderTraversal(root1)
print(f"The Level-Order Traversal array root1: {traversal_result1}")

sub_node_result1 = levelOrderTraversal(sub_root)
print(f"The Level-Order Traversal array root1: {sub_node_result1}")

sol = Solution()
result1 = sol.isSubTree(root1,sub_root)
print(result1)
from collections import deque

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
    def goodNodes(self,root: TreeNode) -> int:
        def dfs(node,prev_val):
            if not node:
                return 0
            elif node.val >= prev_val:
                return 1 + dfs(node.left,node.val) + dfs(node.right,node.val)
            else:
                return dfs(node.left,prev_val) + dfs(node.right,prev_val)
        return dfs(root,root.val)
sol = Solution()
# Tree1
node11 = TreeNode(3)
node12 = TreeNode(1)
node13 = TreeNode(5)

node14 = TreeNode(1,left=node11)
node15 = TreeNode(4,left=node12,right=node13)

root1 = TreeNode(3,left=node14,right=node15)

traverse_result1 = levelOrderTraversal(root1)
print("Tree 1: ",traverse_result1)

result1 = sol.goodNodes(root1)
print("Good Nodes: ",result1)

# Tree 2
node21 = TreeNode(4)
node22 = TreeNode(2)

node23 = TreeNode(3,left=node21,right=node22)

root2 = TreeNode(3,left=node23)

traverse_result2 = levelOrderTraversal(root2)
print("Tree 2: ",traverse_result2)

result2 = sol.goodNodes(root2)
print("Good Nodes: ",result2)

# Tree 3
root3 = TreeNode(1)
traverse_result3 = levelOrderTraversal(root3)
print("Tree 3: ",traverse_result3)

result3 = sol.goodNodes(root3)
print("Good Nodes: ",result3)
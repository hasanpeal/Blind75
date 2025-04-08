from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        # Inorder traversal sorted the BST
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        dfs(root)
        return nodes[k - 1]
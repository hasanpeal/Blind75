from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        #                            5
        #                           / \
        #        -inf < 3 < 5      3   7     5 < 7 < inf
        #                             / \
        #                            4   8
        # For left child our low bound is alway -inf, upper bound is the parents value
        # For right child low bound parents value, upper bound is +inf
        return self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right)
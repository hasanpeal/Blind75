from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def postorder(root):
            # Use nonlocal to access global variable res
            nonlocal res
            if not root:
                return 0
            # Max in left sub tree, if negative then 0
            leftMax = max(postorder(root.left), 0)
            # Max in right sub tree, if negative then 0
            rightMax = max(postorder(root.right), 0)
            # Adjacent node check if max then update global res
            res = max(res, root.val + leftMax + rightMax)
            # Pass single path max sum for each recursive call
            return root.val + max(leftMax, rightMax)
        postorder(root)
        return res
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            length = len(q)
            nodes = []
            for i in range(length):
                node = q.popleft()
                if node:
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if nodes:
                res.append(nodes)
        return res

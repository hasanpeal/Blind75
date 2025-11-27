from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        index = 0
        def preorder():
            nonlocal index
            if nodes[index] == "N":
                index += 1
                return None
            node = TreeNode(int(nodes[index]))
            index += 1
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()
            
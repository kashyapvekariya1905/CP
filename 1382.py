class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            if not node:
                return []
            return traverse(node.left) + [node.val] + traverse(node.right)
        rst = traverse(root)
        def buildBST(values):
            if not values:
                return None
            mid_index = len(values) // 2
            node = TreeNode(values[mid_index])
            node.left = buildBST(values[:mid_index])
            node.right = buildBST(values[mid_index+1:])
            return node
        return buildBST(rst)
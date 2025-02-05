class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            nonlocal total
            if node:
                traverse(node.right)
                total += node.val
                node.val = total
                traverse(node.left)

        total = 0
        traverse(root)
        return root
    
    def printin(self, node):
        if node:
            self.printin(node.left)
            print(node.val, end=' ')
            self.printin(node.right)

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

s = Solution()
new_root = s.bstToGst(root)

s.printin(new_root)
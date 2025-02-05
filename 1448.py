class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stk = [(root,float('-inf'))]
        while stk:
            node,large = stk.pop()
            if large < node.val:
                good +=1
            large = max(large,node.val)
            if node.right: stk.append((node.right,large))
            if node.left: stk.append((node.left,large))
        return good
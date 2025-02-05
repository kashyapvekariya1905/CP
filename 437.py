from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def suma(root,csum):
            if root == None: return 0
            res = 0
            if root.val == csum: res+=1
            res+=suma(root.left,csum-root.val)
            res+=suma(root.right,csum-root.val)
            return res
        if root == None: return 0
        return self.pathSum(root.left,targetSum) + suma(root,targetSum) + self.pathSum(root.right,targetSum)
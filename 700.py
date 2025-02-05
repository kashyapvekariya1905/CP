
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
            
        if root.val == val:
            return root
        elif val<root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
s = Solution()
root = [4,2,7,1,3]
val = 2
print(s.searchBST(root,val))
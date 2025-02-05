# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive approach
        def recursive(node, result):
            if not node:
                return
            recursive(node.left, result)
            recursive(node.right, result)
            result.append(node.val)
        
        result = []
        recursive(root, result)
        return result

    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result[::-1]
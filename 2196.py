# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def construct_tree(cnv):
            nn = TreeNode(cnv)
            if cnv in chmap:
                if chmap[cnv][0] is not None:
                    nn.left = construct_tree(chmap[cnv][0])
                if chmap[cnv][1] is not None:
                    nn.right = construct_tree(chmap[cnv][1])
            return nn

        cs = set()
        chmap: dict[int, list[int]] = {}

        for parent, child, isleft in descriptions:
            if not parent in chmap:
                chmap[parent] = [None, None]
            cs.add(child)
            target = 0 if isleft else 1
            chmap[parent][target] = child

        for parent in chmap:
            if parent not in cs:
                head_node_val: int = parent
                break
        head = construct_tree(head_node_val)
        return head
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res, tmp = [], root
        # stack = []
        # while tmp:
        #     res.append(tmp)
        #     if tmp.right:
        #         stack.append(tmp.right)
        #     elif tmp.left:
        #         stack.append(tmp.left)
        # tmp = tmp.right

        level = []
        stack = [root]
        if root is None:
            return
        while stack:
            tmplist = [i for i in stack]
            stack = []
            for i in tmplist:
                if i.left != None:
                    stack.append(i.left)
                if i.right is not None:
                    stack.append(i.right)
            level.append(tmplist)

        res = []
        for k in level:
            res.append(k[-1].val)
        return res

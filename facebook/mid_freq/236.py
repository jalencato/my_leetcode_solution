# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     stack = [root]
    #     track = collections.defaultdict(list)
    #     track[root] = None
    #     while(True):
    #         tmp = stack.pop()
    #         if tmp.left:
    #             stack.append(tmp.left)
    #             track[tmp.left] = tmp
    #         if tmp.right:
    #             stack.append(tmp.right)
    #             track[tmp.right] = tmp
    #         if p in track and q in track:
    #             break
    #
    #     anc = []
    #     while p:
    #         anc.append(p)
    #         p = track[p]
    #     while q not in anc:
    #         q = track[q]
    #
    #     return q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left and right is None:
            return left
        return right


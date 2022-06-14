"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def dfs(node):
            nonlocal head, tail

            # base case
            if node:
                # left
                dfs(node.left)

                # node
                if tail:
                    node.left = tail
                    tail.right = node
                else:
                    head = node
                tail = node

                # right
                dfs(node.right)

        if not root:
            return None

        head = None
        tail = None
        dfs(root)
        tail.right = head
        head.left = tail
        return head
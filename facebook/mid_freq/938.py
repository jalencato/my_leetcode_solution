class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        res = 0
        stack.append(root)
        while len(stack)!=0:
            tmp = stack.pop()
            if high >= tmp.val >= low:
                res += tmp.val
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return res
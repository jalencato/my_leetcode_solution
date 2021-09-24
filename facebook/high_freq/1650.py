class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def depth_node(p: 'Node'):
            length = 0
            while p:
                length += 1
                p = p.parent
            return length

        max_node = p if depth_node(p) > depth_node(q) else q
        min_node = q if depth_node(p) > depth_node(q) else p
        len_max = depth_node(max_node)
        len_min = depth_node(min_node)
        while len_max > len_min:
            len_max -= 1
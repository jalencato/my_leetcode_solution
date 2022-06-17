def lca(node):
    """Return lowest common ancestor of start and dest nodes."""
    if not node or node.val in (startValue, destValue): return node
    left, right = lca(node.left), lca(node.right)
    return node if left and right else left or right
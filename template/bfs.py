def bfs(root):
    queue=[]
    visited = set()
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

	while queue is not None:
	    cur = queue.pop()
        visited.add(cur)
	    if cur is valid and not visited[cur]:
	    #     ...
	    for n in cur.adjacent：
	        if n is valid：
	            queue.push(n)

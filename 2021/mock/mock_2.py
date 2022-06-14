class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        point = head
        stack = []
        while point is not None:
            stack.append(point)
            point = point.getNext()
        while stack:
            cur = stack.pop()
            cur.printValue()
        return

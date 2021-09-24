# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        # We're at the end of the sum, and can finish the returned List by returning None
        if l1 is None and l2 is None and c == 0: return None

        # We're at the end but still have a leftover carry so need to return an addional 1
        if l1 is None and l2 is None and c > 0: return ListNode(val=1)

        # Handles lists of different lengths by initializing a dummy ListNode if one of them is None
        # If both are None, that is already handled above
        if l1 is None: l1 = ListNode(val=0)
        if l2 is None: l2 = ListNode(val=0)

        # Create preliminary sum
        val = l1.val + l2.val + c

        # Set the final val and carry params for this iteration
        c = 1 if val >= 10 else 0
        val = val - 10 if val >= 10 else val

        # Recurse to the next item in the list
        return ListNode(val=val, next=self.addTwoNumbers(l1.next, l2.next, c=c))
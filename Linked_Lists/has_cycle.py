"""
Linked List Cycle  (Easy)
LeetCode #141  -  Topic: Linked Lists

Approach: see function docstring / inline comments.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next
def build_list(vals):
    head = cur = None
    for v in vals:
        n = ListNode(v)
        if cur: cur.next = n
        else: head = n
        cur = n
    return head
def list_to_list(node):
    out = []
    while node:
        out.append(node.val); node = node.next
    return out
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
        if slow is fast: return True
    return False

if __name__ == "__main__":
    assert has_cycle(build_list([3,2,0,-4])) is False
    print("OK - has_cycle")

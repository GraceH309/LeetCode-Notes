"""
Reverse Linked List  (Easy)
LeetCode #206  -  Topic: Linked Lists

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
def reverse_list(head):
    prev = None
    while head:
        nxt = head.next; head.next = prev; prev = head; head = nxt
    return prev

if __name__ == "__main__":
    h = build_list([1,2,3,4,5])
    assert list_to_list(reverse_list(h)) == [5,4,3,2,1]
    print("OK - reverse_list")

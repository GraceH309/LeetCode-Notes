"""
Remove Nth Node From End  (Medium)
LeetCode #19  -  Topic: Linked Lists

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
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head); fast = slow = dummy
    for _ in range(n + 1): fast = fast.next
    while fast:
        slow = slow.next; fast = fast.next
    slow.next = slow.next.next
    return dummy.next

if __name__ == "__main__":
    h = build_list([1,2,3,4,5])
    assert list_to_list(remove_nth_from_end(h, 2)) == [1,2,3,5]
    print("OK - remove_nth_from_end")

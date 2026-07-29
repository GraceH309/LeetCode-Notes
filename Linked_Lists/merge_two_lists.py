"""
Merge Two Sorted Lists  (Easy)
LeetCode #21  -  Topic: Linked Lists

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
def merge_two_lists(l1, l2):
    dummy = ListNode(); cur = dummy
    while l1 and l2:
        if l1.val < l2.val: cur.next, l1 = l1, l1.next
        else: cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

if __name__ == "__main__":
    a = build_list([1,2,4]); b = build_list([1,3,4])
    assert list_to_list(merge_two_lists(a, b)) == [1,1,2,3,4,4]
    print("OK - merge_two_lists")

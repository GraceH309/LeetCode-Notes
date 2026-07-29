"""
Add Two Numbers  (Medium)
LeetCode #2  -  Topic: Linked Lists

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
def add_two_numbers(l1, l2):
    dummy = cur = ListNode(); carry = 0
    while l1 or l2 or carry:
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry, val = divmod(s, 10)
        cur.next = ListNode(val); cur = cur.next
        l1 = l1.next if l1 else None; l2 = l2.next if l2 else None
    return dummy.next

if __name__ == "__main__":
    a = build_list([2,4,3]); b = build_list([5,6,4])
    assert list_to_list(add_two_numbers(a, b)) == [7,0,8]
    print("OK - add_two_numbers")

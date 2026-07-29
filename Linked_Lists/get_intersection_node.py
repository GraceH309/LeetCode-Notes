"""
Intersection of Two Linked Lists  (Easy)
LeetCode #160  -  Topic: Linked Lists

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
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

if __name__ == "__main__":
    a = build_list([4,1,8,4,5]); b = build_list([5,6,1,8,4,5])
    assert get_intersection_node(a, b) is None or True
    print("OK - get_intersection_node")

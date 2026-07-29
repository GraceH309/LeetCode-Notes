"""
Middle of the Linked List  (Easy)
LeetCode #876  -  Topic: Linked Lists

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
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    return slow

if __name__ == "__main__":
    h = build_list([1,2,3,4,5])
    assert middle_node(h).val == 3
    print("OK - middle_node")

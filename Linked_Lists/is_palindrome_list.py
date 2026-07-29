"""
Palindrome Linked List  (Easy)
LeetCode #234  -  Topic: Linked Lists

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
def is_palindrome(head):
    vals = []
    while head:
        vals.append(head.val); head = head.next
    return vals == vals[::-1]

if __name__ == "__main__":
    assert is_palindrome(build_list([1,2,2,1])) is True
    assert is_palindrome(build_list([1,2])) is False
    print("OK - is_palindrome_list")

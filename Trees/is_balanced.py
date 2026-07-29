"""
Balanced Binary Tree  (Easy)
LeetCode #110  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def is_balanced(root):
    def h(n):
        if not n: return 0
        l = h(n.left); r = h(n.right)
        if l == -1 or r == -1 or abs(l-r) > 1: return -1
        return 1 + max(l, r)
    return h(root) != -1

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(r) is True
    r2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    assert is_balanced(r2) is False
    print("OK - is_balanced")

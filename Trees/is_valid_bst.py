"""
Validate Binary Search Tree  (Medium)
LeetCode #98  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def is_valid_bst(root):
    def ok(n, lo, hi):
        if not n: return True
        if not (lo < n.val < hi): return False
        return ok(n.left, lo, n.val) and ok(n.right, n.val, hi)
    return ok(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    bad = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(bad) is False
    print("OK - is_valid_bst")

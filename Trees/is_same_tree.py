"""
Same Tree  (Easy)
LeetCode #100  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def is_same_tree(p, q):
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == "__main__":
    a = TreeNode(1, TreeNode(2), TreeNode(3)); b = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(a, b) is True
    print("OK - is_same_tree")

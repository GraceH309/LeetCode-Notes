"""
Symmetric Tree  (Easy)
LeetCode #101  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def is_symmetric(root):
    def eq(a, b):
        if not a and not b: return True
        if not a or not b or a.val != b.val: return False
        return eq(a.left, b.right) and eq(a.right, b.left)
    return eq(root.left, root.right) if root else True

if __name__ == "__main__":
    r = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric(r) is True
    print("OK - is_symmetric")

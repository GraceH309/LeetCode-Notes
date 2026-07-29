"""
Invert Binary Tree  (Easy)
LeetCode #226  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

if __name__ == "__main__":
    r = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv = invert_tree(r)
    assert inv.left.val == 7 and inv.right.val == 2
    print("OK - invert_tree")

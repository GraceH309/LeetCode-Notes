"""
Maximum Depth of Binary Tree  (Easy)
LeetCode #104  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def max_depth(root):
    return 0 if not root else 1 + max(max_depth(root.left), max_depth(root.right))

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(r) == 3
    print("OK - max_depth")

"""
Diameter of Binary Tree  (Easy)
LeetCode #543  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def diameter_of_binary_tree(root):
    best = 0
    def depth(n):
        nonlocal best
        if not n: return 0
        l, r = depth(n.left), depth(n.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    depth(root)
    return best

if __name__ == "__main__":
    r = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(r) == 3
    print("OK - diameter_of_binary_tree")

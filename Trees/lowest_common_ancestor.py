"""
Lowest Common Ancestor of BST  (Easy)
LeetCode #235  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def lowest_common_ancestor(root, p, q):
    while root:
        if root.val < p.val and root.val < q.val: root = root.right
        elif root.val > p.val and root.val > q.val: root = root.left
        else: return root
    return None

if __name__ == "__main__":
    r = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8))
    assert lowest_common_ancestor(r, r.left, r.left.right).val == 2
    print("OK - lowest_common_ancestor")

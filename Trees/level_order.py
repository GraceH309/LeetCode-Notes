"""
Binary Tree Level Order Traversal  (Medium)
LeetCode #102  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def level_order(root):
    if not root: return []
    out, q = [], [root]
    while q:
        out.append([n.val for n in q])
        q = [c for n in q for c in (n.left, n.right) if c]
    return out

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(r) == [[3],[9,20],[15,7]]
    print("OK - level_order")

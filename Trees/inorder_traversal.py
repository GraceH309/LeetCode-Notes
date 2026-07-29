"""
Binary Tree Inorder Traversal  (Easy)
LeetCode #94  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def inorder_traversal(root):
    out, st, cur = [], [], root
    while cur or st:
        while cur: st.append(cur); cur = cur.left
        cur = st.pop(); out.append(cur.val); cur = cur.right
    return out

if __name__ == "__main__":
    r = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(r) == [1,3,2]
    print("OK - inorder_traversal")

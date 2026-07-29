"""
Path Sum  (Easy)
LeetCode #112  -  Topic: Trees

Approach: see function docstring / inline comments.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
def has_path_sum(root, target):
    if not root: return False
    if not root.left and not root.right: return root.val == target
    return has_path_sum(root.left, target-root.val) or has_path_sum(root.right, target-root.val)

if __name__ == "__main__":
    r = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4)))
    assert has_path_sum(r, 22) is True
    print("OK - has_path_sum")

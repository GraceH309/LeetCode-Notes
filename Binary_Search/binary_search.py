"""
Binary Search  (Easy)
LeetCode #704  -  Topic: Binary Search

Approach: see function docstring / inline comments.
"""
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        elif nums[m] < target: l = m + 1
        else: r = m - 1
    return -1

if __name__ == "__main__":
    assert binary_search([-1,0,3,5,9,12], 9) == 4
    print("OK - binary_search")

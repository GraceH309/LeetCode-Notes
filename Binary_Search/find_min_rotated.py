"""
Find Minimum in Rotated Sorted Array  (Medium)
LeetCode #153  -  Topic: Binary Search

Approach: see function docstring / inline comments.
"""
def find_min(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]: l = m + 1
        else: r = m
    return nums[l]

if __name__ == "__main__":
    assert find_min([3,4,5,1,2]) == 1
    print("OK - find_min_rotated")

"""
Search in Rotated Sorted Array  (Medium)
LeetCode #33  -  Topic: Binary Search

Approach: see function docstring / inline comments.
"""
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]: r = m - 1
            else: l = m + 1
        else:
            if nums[m] < target <= nums[r]: l = m + 1
            else: r = m - 1
    return -1

if __name__ == "__main__":
    assert search([4,5,6,7,0,1,2], 0) == 4
    print("OK - search_rotated")

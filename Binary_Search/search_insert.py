"""
Search Insert Position  (Easy)
LeetCode #35  -  Topic: Binary Search

Approach: see function docstring / inline comments.
"""
def search_insert(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target: l = m + 1
        else: r = m
    return l

if __name__ == "__main__":
    assert search_insert([1,3,5,6], 5) == 2
    assert search_insert([1,3,5,6], 2) == 1
    print("OK - search_insert")

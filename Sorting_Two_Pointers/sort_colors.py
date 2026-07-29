"""
Sort Colors  (Medium)
LeetCode #75  -  Topic: Sorting & Two Pointers

Approach: see function docstring / inline comments.
"""
def sort_colors(nums):
    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]; lo += 1; mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[hi] = nums[hi], nums[mid]; hi -= 1
        else:
            mid += 1
    return nums

if __name__ == "__main__":
    assert sort_colors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
    print("OK - sort_colors")

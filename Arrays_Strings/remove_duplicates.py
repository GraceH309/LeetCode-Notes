"""
Remove Duplicates from Sorted Array  (Easy)
LeetCode #26  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def remove_duplicates(nums):
    if not nums: return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]; k += 1
    return k

if __name__ == "__main__":
    assert remove_duplicates([1,1,2]) == 2
    assert remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    print("OK - remove_duplicates")

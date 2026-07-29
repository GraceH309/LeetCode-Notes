"""
Move Zeroes  (Easy)
LeetCode #283  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def move_zeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]; j += 1
    return nums

if __name__ == "__main__":
    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    print("OK - move_zeroes")

"""
Contains Duplicate  (Easy)
LeetCode #217  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    print("OK - contains_duplicate")

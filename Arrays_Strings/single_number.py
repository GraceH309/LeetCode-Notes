"""
Single Number  (Easy)
LeetCode #136  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def single_number(nums):
    x = 0
    for n in nums: x ^= n
    return x

if __name__ == "__main__":
    assert single_number([2,2,1]) == 1
    assert single_number([4,1,2,1,2]) == 4
    print("OK - single_number")

"""
Longest Increasing Subsequence  (Medium)
LeetCode #300  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def length_of_lis(nums):
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            m = (lo + hi) // 2
            if tails[m] < x: lo = m + 1
            else: hi = m
        if lo == len(tails): tails.append(x)
        else: tails[lo] = x
    return len(tails)

if __name__ == "__main__":
    assert length_of_lis([10,9,2,5,3,7,101,18]) == 4
    print("OK - length_of_lis")

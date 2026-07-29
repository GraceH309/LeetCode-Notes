"""
House Robber  (Medium)
LeetCode #198  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def rob(nums):
    prev = cur = 0
    for x in nums:
        prev, cur = cur, max(cur, prev + x)
    return cur

if __name__ == "__main__":
    assert rob([2,7,9,3,1]) == 12
    print("OK - rob")

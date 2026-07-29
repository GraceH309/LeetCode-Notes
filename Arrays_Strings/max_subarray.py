"""
Maximum Subarray  (Medium) — LeetCode #53 — Topic: Arrays & Strings

Kadane's algorithm. I failed this three times before it stuck: with all-negative
input you can't default to 0. My first version did `cur = 0` init, so [-2, -1]
returned 0 when it should be -1. Fixed by initializing from the first element.
"""


def max_subarray(nums):
    # v1 (wrong): cur = 0, returns 0 on all-negative — deprecated
    # v2 (right): init from nums[0]
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([-2, -1]) == -1  # all-negative case, where I used to fail
    print("OK - max_subarray")

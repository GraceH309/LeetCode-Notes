"""
Maximum Product Subarray  (Medium)
LeetCode #152  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def max_product(nums):
    best = cur_max = cur_min = nums[0]
    for x in nums[1:]:
        if x < 0: cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max * x); cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best

if __name__ == "__main__":
    assert max_product([2,3,-2,4]) == 6
    print("OK - max_product")

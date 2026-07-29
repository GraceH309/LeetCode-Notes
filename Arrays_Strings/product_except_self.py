"""
Product of Array Except Self  (Medium)
LeetCode #238  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def product_except_self(nums):
    n = len(nums); out = [1]*n
    l = 1
    for i in range(n):
        out[i] = l; l *= nums[i]
    r = 1
    for i in range(n-1, -1, -1):
        out[i] *= r; r *= nums[i]
    return out

if __name__ == "__main__":
    assert product_except_self([1,2,3,4]) == [24,12,8,6]
    print("OK - product_except_self")

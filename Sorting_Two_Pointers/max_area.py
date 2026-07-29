"""
Container With Most Water  (Medium)
LeetCode #11  -  Topic: Sorting & Two Pointers

Approach: see function docstring / inline comments.
"""
def max_area(height):
    l, r = 0, len(height) - 1; best = 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]: l += 1
        else: r -= 1
    return best

if __name__ == "__main__":
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    print("OK - max_area")

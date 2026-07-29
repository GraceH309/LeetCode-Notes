"""
Intersection of Two Arrays II  (Easy)
LeetCode #350  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def intersect(nums1, nums2):
    from collections import Counter
    c = Counter(nums1); out = []
    for x in nums2:
        if c.get(x, 0) > 0:
            out.append(x); c[x] -= 1
    return out

if __name__ == "__main__":
    assert sorted(intersect([1,2,2,1],[2,2])) == [2,2]
    print("OK - intersect")

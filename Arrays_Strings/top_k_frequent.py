"""
Top K Frequent Elements  (Medium)
LeetCode #347  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def top_k_frequent(nums, k):
    from collections import Counter
    freq = Counter(nums)
    return [x for x, _ in freq.most_common(k)]

if __name__ == "__main__":
    assert top_k_frequent([1,1,1,2,2,3], 2) == [1,2]
    print("OK - top_k_frequent")

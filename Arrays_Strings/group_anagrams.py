"""
Group Anagrams  (Medium)
LeetCode #49  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def group_anagrams(strs):
    from collections import defaultdict
    d = defaultdict(list)
    for s in strs:
        d[tuple(sorted(s))].append(s)
    return list(d.values())

if __name__ == "__main__":
    assert sorted(group_anagrams(["eat","tea","tan","ate","nat","bat"])) == [["bat"],["eat","tea","ate"],["tan","nat"]]
    print("OK - group_anagrams")

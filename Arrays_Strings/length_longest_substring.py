"""
Longest Substring Without Repeating Characters  (Medium)
LeetCode #3  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def length_of_longest_substring(s):
    last = {}; start = best = 0
    for i, c in enumerate(s):
        if c in last and last[c] >= start:
            start = last[c] + 1
        last[c] = i
        best = max(best, i - start + 1)
    return best

if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    print("OK - length_longest_substring")

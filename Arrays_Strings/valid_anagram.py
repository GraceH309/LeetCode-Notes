"""
Valid Anagram  (Easy)
LeetCode #242  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def is_anagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    print("OK - valid_anagram")

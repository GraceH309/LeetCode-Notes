"""
Valid Palindrome  (Easy)
LeetCode #125  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def is_palindrome(s):
    t = [c.lower() for c in s if c.isalnum()]
    return t == t[::-1]

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    print("OK - valid_palindrome")

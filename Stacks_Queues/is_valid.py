"""
Valid Parentheses  (Easy)
LeetCode #20  -  Topic: Stacks & Queues

Approach: see function docstring / inline comments.
"""
def is_valid(s):
    st = []; m = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in m:
            if not st or st.pop() != m[c]: return False
        else:
            st.append(c)
    return not st

if __name__ == "__main__":
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    print("OK - is_valid")

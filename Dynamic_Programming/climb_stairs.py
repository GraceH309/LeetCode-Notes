"""
Climbing Stairs  (Easy)
LeetCode #70  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def climb_stairs(n):
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    assert climb_stairs(2) == 2; assert climb_stairs(3) == 3
    print("OK - climb_stairs")

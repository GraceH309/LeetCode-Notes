"""
Unique Paths  (Medium)
LeetCode #62  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def unique_paths(m, n):
    dp = [1]*n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[-1]

if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    print("OK - unique_paths")

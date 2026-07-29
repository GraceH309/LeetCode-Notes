"""
Edit Distance  (Hard)
LeetCode #72  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def min_distance(w1, w2):
    n, m = len(w1), len(w2)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]; dp[0] = i
        for j in range(1, m + 1):
            cur = dp[j]
            dp[j] = prev if w1[i-1] == w2[j-1] else 1 + min(prev, dp[j], dp[j-1])
            prev = cur
    return dp[m]

if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    print("OK - min_distance")

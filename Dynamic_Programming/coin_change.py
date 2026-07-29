"""
Coin Change  (Medium)
LeetCode #322  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1); dp[0] = 0
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] = min(dp[x], dp[x-c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    assert coin_change([1,2,5], 11) == 3
    print("OK - coin_change")

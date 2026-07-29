"""
Best Time to Buy and Sell Stock  (Easy)
LeetCode #121  -  Topic: Arrays & Strings

Approach: see function docstring / inline comments.
"""
def max_profit(prices):
    best = 0; low = float('inf')
    for p in prices:
        low = min(low, p)
        best = max(best, p - low)
    return best

if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print("OK - best_time_stock")

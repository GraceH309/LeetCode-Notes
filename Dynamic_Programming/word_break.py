"""
Word Break  (Medium)
LeetCode #139  -  Topic: Dynamic Programming

Approach: see function docstring / inline comments.
"""
def word_break(s, wordDict):
    words = set(wordDict); dp = [True] + [False]*len(s)
    for i in range(1, len(s)+1):
        for w in words:
            if i >= len(w) and s[i-len(w):i] in words and dp[i-len(w)]:
                dp[i] = True; break
    return dp[-1]

if __name__ == "__main__":
    assert word_break("leetcode", ["leet","code"]) is True
    print("OK - word_break")

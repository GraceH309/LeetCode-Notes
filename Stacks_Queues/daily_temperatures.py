"""
Daily Temperatures  (Medium)
LeetCode #739  -  Topic: Stacks & Queues

Approach: see function docstring / inline comments.
"""
def daily_temperatures(t):
    out = [0]*len(t); st = []
    for i, x in enumerate(t):
        while st and x > t[st[-1]]:
            j = st.pop(); out[j] = i - j
        st.append(i)
    return out

if __name__ == "__main__":
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    print("OK - daily_temperatures")

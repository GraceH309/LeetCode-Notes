"""
Merge Intervals  (Medium)
LeetCode #56  -  Topic: Sorting & Two Pointers

Approach: see function docstring / inline comments.
"""
def merge(intervals):
    intervals.sort()
    out = []
    for s, e in intervals:
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out

if __name__ == "__main__":
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    print("OK - merge_intervals")

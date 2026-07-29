"""
Course Schedule  (Medium)
LeetCode #207  -  Topic: Graphs

Approach: see function docstring / inline comments.
"""
def can_finish(numCourses, prerequisites):
    from collections import deque, defaultdict
    ind = [0]*numCourses; g = defaultdict(list)
    for a, b in prerequisites:
        g[b].append(a); ind[a] += 1
    q = deque(i for i in range(numCourses) if ind[i] == 0)
    seen = 0
    while q:
        n = q.popleft(); seen += 1
        for m in g[n]:
            ind[m] -= 1
            if ind[m] == 0: q.append(m)
    return seen == numCourses

if __name__ == "__main__":
    assert can_finish(2, [[1,0]]) is True
    assert can_finish(2, [[1,0],[0,1]]) is False
    print("OK - can_finish")

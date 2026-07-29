"""
Rotting Oranges  (Medium)
LeetCode #994  -  Topic: Graphs

Approach: see function docstring / inline comments.
"""
def oranges_rotting(grid):
    from collections import deque
    R, C = len(grid), len(grid[0]); q = deque(); fresh = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2: q.append((i,j,0))
            elif grid[i][j] == 1: fresh += 1
    t = 0
    while q:
        i, j, t = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0<=ni<R and 0<=nj<C and grid[ni][nj] == 1:
                grid[ni][nj] = 2; q.append((ni,nj,t+1)); fresh -= 1
    return t if fresh == 0 else -1

if __name__ == "__main__":
    assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    print("OK - oranges_rotting")

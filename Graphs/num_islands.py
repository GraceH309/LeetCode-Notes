"""
Number of Islands  (Medium)
LeetCode #200  -  Topic: Graphs

Approach: see function docstring / inline comments.
"""
def num_islands(grid):
    if not grid: return 0
    R, C = len(grid), len(grid[0])
    def dfs(r, c):
        if r<0 or c<0 or r>=R or c>=C or grid[r][c] != '1': return
        grid[r][c] = '#'
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)): dfs(r+dr, c+dc)
    cnt = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '1':
                dfs(i, j); cnt += 1
    return cnt

if __name__ == "__main__":
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g) == 3
    print("OK - num_islands")

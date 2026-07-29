"""
Pacific Atlantic Water Flow  (Medium)
LeetCode #417  -  Topic: Graphs

Approach: see function docstring / inline comments.
"""
def pacific_atlantic(heights):
    if not heights: return []
    R, C = len(heights), len(heights[0])
    def bfs(ocean):
        q = ocean; seen = set(ocean)
        while q:
            i, j = q.pop()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0<=ni<R and 0<=nj<C and (ni,nj) not in seen and heights[ni][nj] >= heights[i][j]:
                    seen.add((ni,nj)); q.append((ni,nj))
        return seen
    top = [(0,j) for j in range(C)] + [(i,0) for i in range(R)]
    bot = [(R-1,j) for j in range(C)] + [(i,C-1) for i in range(R)]
    return bfs(top) & bfs(bot)

if __name__ == "__main__":
    h = [[1,2,2,3],[3,2,3,4],[2,4,5,3],[6,7,1,4]]
    assert len(pacific_atlantic(h)) >= 1
    print("OK - pacific_atlantic")

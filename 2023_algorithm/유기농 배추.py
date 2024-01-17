from collections import deque

t = int(input())
answer = []

def dfs(r, c):
    if r < 0 or r >= m or c < 0 or c >= n:
        return
    
    if _map[r][c] == 0:
        return
    
    _map[r][c] = 0
    for x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        dfs(r + x[0], c + x[1])

for _ in range(t):
    num = 0
    m, n, k = list(map(int, input().split()))
    _map = [[0] * n for _ in range(m)]
    for _ in range(k):
        row, col = list(map(int, input().split()))
        _map[row][col] = 1
    
    for r in range(m):
        for c in range(n):
            if _map[r][c] == 1:
                dfs(r, c)
                num += 1
    
    answer.append(num)

for x in answer:
    print(x)

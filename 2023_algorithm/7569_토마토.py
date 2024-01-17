"""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
"""

from collections import deque

M, N, H = list(map(int, input().split()))
tomatos = []
for h in range(H):
    tomatos.append([])
    for n in range(N):
        tomatos[h].append(list(map(int, input().split())))

q = deque([])
MAX_DAY = 0

def bfs():
    global MAX_DAY
    while len(q) != 0:
        height, row, col, day = q.popleft()
        for x in [(-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1)]:  # 위, 아래, 앞, 뒤, 좌, 우
            new_height, new_row, new_col = height + x[0], row + x[1], col + x[2]
            if (0 <= new_height < H) and (0 <= new_row < N) and (0 <= new_col < M) and (tomatos[new_height][new_row][new_col] == 0):
                tomatos[new_height][new_row][new_col] = 1
                MAX_DAY = max(MAX_DAY, day+1)
                q.append((new_height, new_row, new_col, day+1))

for height in range(H):
    for row in range(N):
        for col in range(M):
            if tomatos[height][row][col] == 1:
                q.append((height, row, col, 0))


result = []
if len(q) == 0:
    result.append(-1)
else:
    bfs()
    for height in tomatos:
        for row in height:
            if 0 in row:
                result.append(-1)
    else:
        result.append(MAX_DAY)
print(result[0])

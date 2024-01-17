"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""

from collections import deque

m, n = list(map(int, input().split()))
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

q = deque([])
MAX_DAY = 0

def bfs():
    global MAX_DAY
    while len(q) != 0:
        row, col, day = q.popleft()
        for x in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            new_row, new_col = row + x[0], col + x[1]
            if (0 <= new_row < n) and (0 <= new_col < m) and (map_data[new_row][new_col] == 0):
                map_data[new_row][new_col] = 1
                MAX_DAY = max(MAX_DAY, day+1)
                q.append((new_row, new_col, day+1))

for row in range(n):
    for col in range(m):
        if map_data[row][col] == 1:
            q.append((row, col, 0))

if len(q) == 0:
    print(-1)
else:
    bfs()
    for x in map_data:
        if 0 in x:
            print(-1)
            break
    else:
        print(MAX_DAY)
"""
4 6
101111
101010
101011
111011

4 6
110110
110110
111111
111101
"""

from collections import deque

n, m = list(map(int, input().split()))
map_data = []
for _ in range(n):
    row = list(map(int, list(input())))
    map_data.append(row)

q = [(0, 0)]
q = deque(q)
while len(q) != 0:
    x, y = q.popleft()
    for i in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x_next = x + i[0]
        y_next = y + i[1]
        if 0 <= x_next < n and 0 <= y_next < m:
            if map_data[x_next][y_next] == 1:
                map_data[x_next][y_next] = map_data[x][y] + 1
                q.append((x_next, y_next))

print(map_data[n-1][m-1])
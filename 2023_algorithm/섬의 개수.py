"""
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
"""

def dfs(map_data, boundary, cur_pos):
    x, y = cur_pos
    w, h = boundary
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if map_data[x][y] == 0:
        return

    map_data[x][y] = 0
    for next in [(0, -1), (1, 0), (0, 1), (-1, 0), 
                 (1, -1), (1, 1), (-1, 1), (-1, -1)]:
        next_pos = (x + next[0], y + next[1])
        dfs(map_data, boundary, next_pos)

result = []
while True:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
    map_data = []
    for _ in range(h):
        row = list(map(int, input().split()))
        map_data.append(row)

    map_count = 0
    for x in range(h):
        for y in range(w):
            if map_data[x][y] == 1:
                dfs(map_data, (w, h), (x, y))
                map_count += 1
    result.append(map_count)
    
for x in result:
    print(x)
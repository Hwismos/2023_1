"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""

N = int(input())
picture = []
for _ in range(N):
    picture.append(list(input()))

from collections import deque

def bfs(row, col, color):
    if color == "B":
        picture[row][col] = "0"
    elif color == "R" or color == "G":
        picture[row][col] = "1"
    else:
        picture[row][col] = "0"

    q = deque([(row, col)])

    while len(q) != 0:
        row, col = q.popleft()
        for direction in [(-1,0),(0,1),(1,0),(0,-1)]:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if (0 <= new_row < N) and (0 <= new_col < N) and (picture[new_row][new_col] == color):
                if color == "B":
                    picture[new_row][new_col] = "0"
                elif color == "R" or color == "G":
                    picture[new_row][new_col] = "1"
                else:
                    picture[new_row][new_col] = "0"
                q.append((new_row, new_col))

blue_area = 0
res1 = 0
for row in range(N):
    for col in range(N):
        if picture[row][col] == "B":
            bfs(row, col, "B")
            blue_area += 1
        if picture[row][col] == "R":
            bfs(row, col, "R")
            res1 += 1
        if picture[row][col] == "G":
            bfs(row, col, "G")
            res1 += 1

res2 = 0
for row in range(N):
    for col in range(N):
        if picture[row][col] == "1":
            bfs(row, col, "1")
            res2 += 1

print(f"{res1 + blue_area} {res2 + blue_area}")
"""
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

5 5
2 2 3 
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 1 0 1
1 1 1 1 1
"""

n, m = list(map(int, input().split()))
row, col, d = list(map(int, input().split()))  # row, column, direction
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

result = []
call_stack = []

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def dfs(row, col, direction):
    call_stack.append(f"dfs({row}, {col}, {direction})")
    if map_data[row][col] == 0:
        map_data[row][col] = 2  # done
        result.append((row, col))

    for _ in range(4):
        new_direction = (direction+3) % 4
        new_row = row + dr[new_direction]
        new_col = col + dc[new_direction]
        if map_data[new_row][new_col] == 0:
            dfs(new_row, new_col, new_direction)
            return
        direction = new_direction

    new_direction = (direction + 2) % 4
    new_row = row + dr[new_direction]
    new_col = col + dc[new_direction]
    if map_data[new_row][new_col] == 1:
        return
    else:
        dfs(new_row, new_col, direction)

dfs(row, col, d)

print(len(result))

for x in map_data:
    print(x)

for x in result:
    print(f"{x} →", end = " ")
print()
for x in call_stack:
    print(f"{x} →", end = " ")    
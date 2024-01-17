HOMES = 0

def dfs(x, y, n):
    global HOMES
    data[x][y] = 0
    HOMES += 1
    for i in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x_next = x + i[0]
        y_next = y + i[1]
        if 0 <= x_next < n and 0 <= y_next < n:
            if data[x_next][y_next] == 1:
                dfs(x_next, y_next, n)

n = int(input())
data = []
for _ in range(n):
    x = list(map(int, list(input())))
    data.append(x)

result = []
total_home_num = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            total_home_num += 1
            dfs(i, j, n)
            result.append(HOMES)
            HOMES = 0

result.insert(0, total_home_num)
x = result.pop(0)
print(x)
result.sort()
for y in result:
    print(y)
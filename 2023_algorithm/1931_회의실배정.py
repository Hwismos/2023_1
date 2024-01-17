"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: [x[1], x[0]])

result = []
result.append(data[0])

for i in range(1, n):
    last = result[-1]
    if data[i][0] >= last[1]:
        result.append(data[i])
        last = result[-1]

print(len(result))
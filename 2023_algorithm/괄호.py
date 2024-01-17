t = int(input())
data = []

for _ in range(t):
    data.append(list(input()))

result = []

for i in range(t):
    check_cnt = 0
    for char in data[i]:
        if char == '(':
            check_cnt += 1
        else:
            check_cnt -= 1
        
        if check_cnt < 0:
            break
    if check_cnt == 0:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)
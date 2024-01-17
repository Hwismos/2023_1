T = int(input())
tests = []
for _ in range(T):
    tests.append(list(map(int, input().split())))

for case in tests:
    x, y = case
    distance = y - x
    n = 0

    while True:
        if distance <= n*(n+1):
            break
        n += 1
    
    if distance <= n ** 2:
        print(2 * n - 1)
    else:
        print(2 * n)
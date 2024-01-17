# 10000까지의 수에 대해 에라토스테네시의 체를 적용한다.
m = 10001
arr = [1 for _ in range(m)]  # 해당 인덱스가 소수이면 1로 가정한다.
for i in range(2, m):
    for j in range(2, m):
        if (i * j) >= m:
            break
        else:
            arr[i * j] = 0
arr[:2] = [0, 0]

# 에라토스테네스의 체를 이용해 n의 파티션을 구한다.
T = int(input())
results = []
for _ in range(T):
    n = int(input())
    diff = 1e9

    primes = []
    for i in range(0, n):
        if arr[i] == 1:
            primes.append(i)
    
    a, b = n//2, n//2
    while a > 0:
        if a in primes and b in primes:
            results.append((a, b))
            break
        else:
            a -= 1
            b += 1

for res in results:
    print(f"{res[0]} {res[1]}")

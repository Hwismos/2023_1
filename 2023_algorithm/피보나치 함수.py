T = int(input())
answer = []

dp = [0] * 41
dp[0] = 1
dp[1] = 1

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(T):
    N = int(input())
    if N == 0:
        answer.append((1, 0))
    elif N == 1:
        answer.append((0, 1))
    else:
        answer.append((dp[N-2], dp[N-1]))


for x in answer:
    print(f'{x[0]} {x[1]}')


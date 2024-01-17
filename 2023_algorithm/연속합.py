n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]
max_value = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i], data[i])
    if max_value < dp[i]:
        max_value = dp[i]

print(max_value)
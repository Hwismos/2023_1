'''
6
10 20 10 30 20 50
'''

a = int(input())
seq = list(map(int, input().split()))

dp = [1] * a

for i in range(a):
    if i == 0:
        continue
    max_LIS = -1e9
    for j in range(i, -1, -1):
        if seq[i] > seq[j]:
            if max_LIS < dp[j]:
                max_LIS = dp[j]
                dp[i] = max_LIS + 1

print(max(dp))
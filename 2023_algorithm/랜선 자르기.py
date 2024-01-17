'''
802
743
457
539
'''

k, n = list(map(int, input().split()))
data = []
for _ in range(k):
    x = int(input())
    data.append(x)

left = 1
right = max(data)

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for x in data:
        cnt += x // mid
    # print(f'자르고자 하는 랜선의 길이: {mid}, 랜선의 개수: {cnt}')
    if cnt < n:
        right = mid - 1
    if cnt >= n:
        left = mid + 1

# print(f'최대 랜선의 길이: {mid}')
print(right)
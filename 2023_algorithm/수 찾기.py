n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int,input().split()))

data1.sort()
n_length = len(data1)
result = []

def binary_search(target):
    mid = n_length // 2
    left, right = 0, (n_length - 1)
    while target != data1[mid]:
        if left > right:
            mid = -1
            break
        elif target > data1[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    if mid == -1:
        return False
    return True

for data in data2:
    answer = binary_search(data)
    if answer == True:
        result.append(1)
    else:
        result.append(0)

for data in result:
    print(data)
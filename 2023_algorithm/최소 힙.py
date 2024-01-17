# class Node():
#     def __init__(self, value, left=None, right=None):
#         self.left = left
#         self.right = right
#         self.value = value

# def push(parent, cur):
#     if parent.left == None and parent.right == None:
#         parent.left = cur
#     elif parent.left != None and parent.right == None:
#         parent.right = cur
#     else:
#         push(parent.left, cur)

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# push(n1, n2)
# push(n1, n3)

# print(n1.value)

import heapq

min_heap = []
result = []
n = int(input())
for _ in range(n):
    data = int(input())
    if data == 0:
        if len(min_heap) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, data)

for x in result:
    print(x)
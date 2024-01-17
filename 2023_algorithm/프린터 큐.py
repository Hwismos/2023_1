from collections import deque

T = int(input())
answer = []
for i in range(T):
    N, target = list(map(int, input().split()))
    docs = list(map(int, input().split()))
    docs_tuple = []

    for i in range(len(docs)):
        docs_tuple.append((i, docs[i])) 
    
    q = deque(docs_tuple)

    count = 0
    while len(q) != 0:
        max_value = -1e9
        for cur in q:
            if max_value < cur[1]:
                max_value = cur[1]
        
        cur = q.popleft()

        if cur[1] < max_value:
            q.append(cur)
        else:
            count+=1
            if target == cur[0]:
                answer.append(count)
for x in answer:
    print(x)

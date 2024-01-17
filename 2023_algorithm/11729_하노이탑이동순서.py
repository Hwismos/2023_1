result = []

def recursion(n, start, end):
    if n == 1:
        result.append(f"{start} {end}")
        return
    
    recursion(n-1, start, 6-start-end)
    result.append(f"{start} {end}")
    recursion(n-1, 6-start-end, end)
    

N = int(input())
recursion(N, 1, 3)

print(len(result))
for x in result:
    print(x)
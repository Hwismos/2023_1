n = int(input())
stack = []
result = []

for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        stack.append(int(cmd[1]))
    else:
        cmd = cmd[0]
        if cmd == 'pop':
            if len(stack) == 0:
                result.append(-1)
            else:
                poped = stack.pop()
                result.append(poped)
        elif cmd == 'size':
            result.append(len(stack))
        elif cmd == 'empty':
            if len(stack) == 0:
                result.append(1)
            else:
                result.append(0)
        else:
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])

for i in result:
    print(i)

data = list(input())

result = 0
sticks = 0
for x in data:
    if x == "(":
        sticks += 1
    if x == ")":
        if prev_x == "(":
            if sticks > 0:
                sticks -= 1
            result += sticks
        if prev_x == ")":
            sticks -= 1
            result += 1
    prev_x = x

print(result)
n = int(input())
answer = []
seq = []
for _ in range(n):
    seq.append(int(input()))

sorted_seq = sorted(seq)
sorted_idx = 0

stack = []
seq_idx = 0
while True:
    if seq_idx == n:
        break

    if len(stack) != 0 and stack[-1] == seq[seq_idx]:
        stack.pop()
        answer.append('-')
        seq_idx += 1
        continue

    if sorted_idx == n:
        answer.clear()
        answer.append('NO')
        break

    stack.append(sorted_seq[sorted_idx])
    answer.append('+')
    sorted_idx += 1

for x in answer:
    print(x)

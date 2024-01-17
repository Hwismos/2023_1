"""
4 6
a t c i s w
"""

L, C = list(map(int, input().split()))
words = sorted(list(input().split()))

result = []

def back_tracking(cnt, idx):
    if cnt == L:
        v, c = 0, 0

        for i in range(L):
            if result[i] in ["a", "e", "i", "o", "u"]:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print("".join(result))
        return

    for i in range(idx, C):
        result.append(words[i])
        back_tracking(cnt + 1, i + 1)
        result.pop()

back_tracking(0, 0)
'''
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
'''
import math

T = int(input())
answer = []

def calc_distance_of_center_point(x1, y1, x2, y2):
    X = math.pow((x1-x2), 2) + math.pow((y1-y2), 2)
    X = math.sqrt(X)
    return X

def check_case(DCP, r1, r2):
    if DCP == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        if DCP <= (max(r1, r2) - min(r1, r2)):
            if DCP == (max(r1, r2) - min(r1, r2)):
                return 1
            else:
                return 0
        else:
            if DCP < r1 + r2:
                return 2
            if DCP == r1 + r2:
                return 1
            if DCP > r1 + r2:
                return 0

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    DCP = calc_distance_of_center_point(x1, y1, x2, y2)
    answer.append(check_case(DCP, abs(r1), abs(r2)))

for x in answer:
    print(x)
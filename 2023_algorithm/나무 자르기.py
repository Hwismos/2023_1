n, m = list(map(int, input().split()))
tree = list(map(int, input().split()))

def cut_tree(mid):
    my_tree = 0
    for t in tree:
        if t >= mid:
            my_tree += t - mid
    return my_tree

def binary_search():
    if m == 0:
        return max(tree)

    left = 0
    right = sum(tree)

    while left <= right:
        mid = (left + right) // 2
        my_tree = cut_tree(mid)
        # print(f'({mid}, {my_tree})')
        if my_tree == m:
            return mid
        if my_tree < m:
            right = mid - 1
        if my_tree > m:
            left = mid + 1
    return (left - 1)

answer = binary_search()
print(answer)
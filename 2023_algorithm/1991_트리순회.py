"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""

N = int(input())
tree = {}
for _ in range(N):
    cur, left, right = input().split()
    tree[cur] = [left, right]

orders = []

def preorder(cur):
    if cur == ".":
        return
    orders.append(cur)
    preorder(tree[cur][0])
    preorder(tree[cur][1])

def inorder(cur):
    if cur == ".":
        return
    inorder(tree[cur][0])
    orders.append(cur)
    inorder(tree[cur][1])

def postorder(cur):
    if cur == ".":
        return
    postorder(tree[cur][0])
    postorder(tree[cur][1])
    orders.append(cur)

preorder("A")
print("".join(orders))
orders.clear()
inorder("A")
print("".join(orders))
orders.clear()
postorder("A")
print("".join(orders))
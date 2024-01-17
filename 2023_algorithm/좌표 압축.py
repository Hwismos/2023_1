"""
5
2 4 -10 4 -9

6
1000 999 1000 999 1000 999
"""

n = int(input())
data = list(map(int, input().split()))
# set 메소드는 해시 테이블을 이용하므로 시간 복잡도는 O(1)이다.
set_data = sorted(list(set(data)))  
# 딕셔너리를 생성하기 위해 O(n)의 연산을 수행한다.
dict_data = {value: idx for idx, value in enumerate(set_data)}
result = []

# 전체 데이터를 조회하므로 O(n)의 연산이 수행된다.
for i in data:
    # 딕셔너리, 해싱을 이용하기 때문에 
    # index를 찾는데에는 O(1)의 시간으로 연산을 수행할 수 있다. 
    idx = dict_data[i]
    result.append(idx)

for x in result:
    print(x)
"""
4
1 2 1 3 3 4 3 5
"""
N = 5
E = int(input())
tree = list(map(int, input().split()))

#1. 인덱스 번호 => 부모노드의 번호
child_left = [0] * (N + 1) 
child_right = [0] * (N + 1)

for i in range(0, E):
    parent = tree[i*2]
    child = tree[i*2+1]
    # 왼쪽 자식이 비어있으면 왼쪽 부터 추가
    if child_left[parent] == 0:
        child_left[parent] = child
    # 왼쪽 자식이 있으면 오른쪽 자식으로 추가
    else:
        child_right[parent] = child

# 2. 인덱스 번호 => 자식노드의 번호

parent = [0] * (N + 1) # parent[i] => i번째 노드의 부모 노드 번호
for i in range(0, E):
    p = tree[i*2]
    c = tree[i*2+1]
    parent[c] = p

print(child_left)
print(child_right)
print(parent)

# 조상노드 찾기
now = 5

while parent[now] != 0:   # 노드번호에 0이 포함 안되있을때
    print(parent[now])
    now = parent[now]
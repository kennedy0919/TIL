"""
1
5 3
1 2
2 3
4 5
"""


def find_set(x):
    if p[x] == x:
        return x
    
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        p[y] = x
    
    else:
        p[x] = y


T = int(input())

for tc in range(1, T + 1):
    P, E = map(int, input().split())
    
    p = [i for i in range(0, P+1)]

    for _ in range(0, E):
        x, y = list(map(int, input().split()))
        union(x, y)
    
    ans = set()
    
    for i in p:
        ans.add(find_set(i))

    print(f"#{tc} {len(ans)-1}")

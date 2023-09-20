"""
1
5 2
1 2 3 4
"""

def find_set(x):
    if p[x] == x:
        return x
    
    text[x] = find_set(p[x])
    return p[x]

def union(x, y):
    global cnt
    x = find_set(x)
    y = find_set(y)

    if x == y:
        cnt = cnt - 1
        return
    
    if x < y:
        p[y] = x
        cnt = cnt - 1
    else:
        p[x] = y
        cnt = cnt - 1
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    text = list(map(int, input().split()))
    cnt = N
    p = [i for i in range(0, N+1)]
    
    for i in range(0, M):
        union(text[2*i], text[2*i+1])

    print(f"#{tc} {cnt}")
    

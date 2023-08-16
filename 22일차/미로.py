def find_end(s):
    for c in range(0, N):
        if arr[0][c] == 3:
            i = c
    visited = [0] * 10
    stack = []
    visited[i] = 3

    while True:
        if i == 2:
            return 1
        for j in range(0, N * N):
            if arr[i][j] == 0 and not visited[j]:
                visited[j] = 1
                stack.append(i)
                i = j
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    
    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    
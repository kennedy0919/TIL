def dfs(s):
    visited = [0] * 100
    stack = []
    i = s
    visited[i] = 1

    while True:
        if i == 99:
            return 1

        for j in range(0, 100):
            if arr[i][j] == 1 and not visited[j]:
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

T = 10
for i in range(1, 1 + T):
    tc, N = map(int, input().split())
    text = list(map(int, input().split()))
    arr = [[0] * 100 for _ in range(0, 100)]
    for k in range(0, N):
        arr[text[k*2]][text[k*2+1]] = 1

    ans = dfs(0)
    print(f"#{tc} {ans}")
        




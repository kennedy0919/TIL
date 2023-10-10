def solve(n, now_sum, cur):
    global ans
    if n == N:
        ans = min(ans, now_sum+arr[cur][1])
        return
     
    for j in range(2, N+1):
        if visited[j] == 0:
            visited[j] = 1
            solve(n+1, now_sum + arr[cur][j], j)
            visited[j] = 0
     
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _  in range(0, N)]
    visited = [0] * (N+1)
    ans = 10000
    solve(1, 0, 1)
    print(f"#{tc} {ans}")
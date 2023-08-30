def solve(r, c, now_sum):
    global min_v
    if r == N-1 and c == N-1:
        min_v = min(min_v, now_sum)
        return
    
    for d in range(0, 2):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc):
            solve(nr, nc, now_sum + arr[nr][nc])

        
def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    min_v = 1000
    dr = [1, 0]
    dc = [0, 1]
    solve(0, 0, arr[0][0])
    print(f"#{tc} {min_v}")
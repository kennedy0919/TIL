T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    ans = 0
    for r in range(0, N):
        for c in range(0, N):
            cnt = 0
            if arr[r][c] == 1:
                for k in range(1, K+1):
                    if c+k < N and arr[r][c+k] == 1:
                        cnt = cnt + 1
                    if cnt == K - 1:
                        if c+k == N-1 or arr[r][c+k+1] == 0:
                            ans = ans + 1
    for c in range(0, N):
        for r in range(0, N):
            cnt = 0
            if arr[r][c] == 1:
                for k in range(1, K+1):
                    if c+k < N and arr[r+k][c] == 1:
                        cnt = cnt + 1
                    if cnt == K - 1:
                        if r+k == N-1 or arr[r+k+1][c] == 0:
                            ans = ans + 1

    print(f"#{tc} {ans}")
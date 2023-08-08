T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())  
    arr = [list(map(str, input().split()))for _ in range(N)]

    for r in range(0, N):
        for c in range(0, N - M + 1):
            counts = 0

            for i in range(0, M):
                if arr[r][c] == arr[r][M - c]:
                    counts = counts + 1
                if arr[r][c] != arr[r][M - c]:
                    break
                if counts == M // 2:
                    ans = " "
                    for c in range(0, M):
                        ans = ans + arr[r][c]

    for c in range(0, N):
        for r in range(0, N - M + 1):
            counts = 0

            for i in range(0, M):
                if arr[r][c] == arr[r][M - r]:
                    counts = counts + 1
                if arr[r][c] != arr[r][M - r]:
                    break
                if counts == M // 2:
                    ans = " "
                    for c in range(0, M):
                        ans = ans + arr[r][c]

    print(f"#{tc} {ans}")
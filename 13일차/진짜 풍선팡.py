T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_cnt = 0

    for r in range(0, N):

        for c in range(0, M):
            cnt = arr[r][c]

            d = 0
            for i in range(0, cnt):
                d = d + i

                for d in range(4):
                    
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < M:
                        cnt = cnt + arr[nr][nc]

                if max_cnt < cnt:
                    max_cnt = cnt

    print(f"#{tc} {max_cnt}")
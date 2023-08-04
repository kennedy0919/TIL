#### 첫번째 case 가 왜 안되는지 모르겠어요

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_cnt = 0

    for r in range(0, N):

        for c in range(0, M):
            cnt = arr[r][c]

        
            for d in range(4):
                for n in range(1, cnt + 1):
                    dr = [-n, n, 0, 0]
                    dc = [0, 0, -n, n]
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < M:
                        cnt = cnt + arr[nr][nc]

            if max_cnt < cnt:
                    max_cnt = cnt

    print(f"#{tc} {max_cnt}")
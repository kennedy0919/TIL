T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    cnt = 0
    max_cnt = 0
    
    for r in range(0, N):
        cnt = 0
        for c in range(0, N):
            if arr[r][c] == 1:
                cnt = cnt + 1
            if arr[r][c] == 0:    
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt

    for c in range(0, N):
        cnt = 0
        for r in range(0, N):
            if arr[r][c] == 1:
                cnt = cnt + 1
            if arr[r][c] == 0:    
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")
        

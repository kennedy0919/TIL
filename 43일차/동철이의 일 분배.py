def solution(row, per):
    global ans
    # 가지치기
    if ans > per:
        return
        
    if row == N:
        if ans < per:
            ans = per
        return
    
    for r in range(0, N):
        # 가지치기
        if arr[row][r] == 0:
            return
        
        can_place = True
        # 세로검사
        for c in range(0, row):
            if visited[c][r] == 1:
                can_place = False
                break
        
        if can_place:
            visited[row][r] = 1
            solution(row+1, per * (arr[row][r] / 100))
            visited[row][r] = 0



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    visited = [[0] * N for _ in range(0, N)]
    ans = 0
    solution(0, 1)
    print(f"#{tc} {'{:.6f}'.format(round(ans*100, 6))}")
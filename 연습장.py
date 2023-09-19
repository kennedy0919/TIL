def backtracking(row):
    global ans
    global sum_num
    # 종료 조건
    if row == N: 
        if ans > sum_num:
            ans = sum_num
        sum_num = 0
        return

    # 현재 row 행에서 i 번째 열에 퀸을 놓을수 있으면 놓고 row+1 행에 퀸 놓으러 가기
    for i in range(0, N):
        # i 번째 행에 퀸을 놓을수 있는가?
        can_place = True

        # 세로에 퀸이 있는지 검사
        for j in range(0, row):
            if visited[j][i] == 1:
                can_place = False
                break

        # 세로와 대각선 검사를 했는데 i 번째 열에 퀸을 놓을 수 있으면
        if can_place:
            ans = ans + cost[row][i]
            # 놓을수 있으면 현재 위치에 놓고 다음 위치로 이동 ==> 재귀 호출
            visited[row][i] = 1
            # row+1 에 퀸 놓으러 가기, 남은 퀸 개수 -1
            
            backtracking(row+1)
            # 다시 되돌려 놓고 진행
            visited[row][i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(0, N)]
    ans = 10000
    sum_num = 0
    visited = [[0] * N for _ in range(0, N)]
    backtracking(0)
    print(f"#{tc} {ans}")
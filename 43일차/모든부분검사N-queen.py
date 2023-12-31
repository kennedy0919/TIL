# row : 현재 행 번호
# remain : 놓아야 할 퀸의 남은 개수

def backtracking(row, remain):
    global cnt
    # 종료 조건
    if row == N and remain == 0: 
        cnt = cnt + 1
        return

    # 현재 row 행에서 i 번째 열에 퀸을 놓을수 있으면 놓고 row+1 행에 퀸 놓으러 가기
    for i in range(0, N):
        # i 번째 행에 퀸을 놓을수 있는가?
        can_place = True

        # 가로검사
        for j in range(0, N):
            if board[row][j] == 1:
                can_place = False
                break
        
        # 세로에 퀸이 있는지 검사
        for j in range(0, row):
            if board[j][i] == 1:
                can_place = False
                break

        # 대각선에 퀸이 있는지 검사
        for j in range(1, row+1):
            # 좌상
            if row - j >= 0 and i - j >= 0 and board[row-j][i-j] == 1:
                can_place = False
                break
            # 우상
            if row - j >= 0 and i + j < N and board[row-j][i+j] == 1:
                can_place = False
                break
        # 세로와 대각선 검사를 했는데 i 번째 열에 퀸을 놓을 수 있으면
        if can_place:
            # 놓을수 있으면 현재 위치에 놓고 다음 위치로 이동 ==> 재귀 호출
            board[row][i] = 1
            # row+1 에 퀸 놓으러 가기, 남은 퀸 개수 -1
            
            backtracking(row+1, remain-1)
            # 다시 되돌려 놓고 진행
            board[row][i] = 0

    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 경우의 수
    cnt = 0

    #보드 만들기
    board = [[0] * N for _ in range(0, N)]
    backtracking(0, N)
    print(f"#{tc} {cnt}")

    
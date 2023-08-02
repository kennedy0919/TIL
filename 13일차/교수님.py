'''
3
5
45 15 10 56 23 
96 98 99 40 69 
96 84 49 46 34 
16 64 81 4 11 
10 66 85 55 14 
5
44 91 64 73 62 
78 72 52 73 48 
44 88 55 75 24 
22 72 59 26 62 
87 11 64 79 40 
5
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10

'''

T = int(input())

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

for tc in range(1, T + 1):
    N = int(input())

    # 상하좌우(델타)
    # (행의 좌표, 열의좌표)
    # (r, c)
    # 0=상 1=하  2=좌 3=우
    # 상 (-1,0) 하 (1,0) 좌(0,-1) 우(0,1) 만큼 변한다.
    dr = [-1, 1, 0, 0] # 행 번호의 변화량
    dc = [0, 0, -1, 1] # 열 번호의 변화량

    # 2차원 배열 입력받기
    # list(....) => 한줄 입력받기 (1차원 배열)
    # for - in range(N) => N 번 입력을 받아서 2차원 배열로 만든다.
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열 탐색
    # 행우선으로

    diff_sum = 0
    for r in range(N): #가로와 세로의 길이가 같으니까 행도 n만큼, 열도 n만큼
        
        for c in range(N):
            # 현재 위치가 r행 c열 (r,c)
            # maxtrix[r][c] => 현재 위치에 저장된 원소
            # print(f"현재위치 : {r}{c}, 값 : {matrix[r][c]}")

            
            # 현재 위치에서 상하좌우 차이 절대값의 합
            now_diff_num = 0

            # 상하좌우 탐색
            # d = 0, 1, 2, 3 으로 변한다
            for d in range(4):
                # d는 델타 배열의 인덱스, d = 0 이면 상...
                # 현재 위치는 (r,c) 상하좌우로 이동 후 위치를 (nr,nc)
                nr = r + dr[d] # 다음 행 번호 = 현재 행 번호 + 이동항향이 d일때 변화량
                nc = c + dc[d] # 다음 열 번호 = 현재 열 번호 + 이동방향이 d일때 변화량 

                # 내가 계산한 위치가 유효한 인덱스인지(배열의 범위 안에 있는지) 검사
            
                if 0 <= nr < N and 0 <= nc < N:
                    # 차이 = 현재 위치에 있는 값 - 움직인 위치에 있는 값
                    diff = matrix[r][c] - matrix[nr][nc]
                    # 절댓값 abs 사용하지 않고 구하기
                    if diff < 0:
                        diff = -diff
                    else:
                        diff = diff

                    now_diff_num += diff
        
            # 상하좌우 탐색이 끝나면 현재 위치 절대값 차이의 합이 구해졌다.
            diff_sum += now_diff_num

    print(f"#{tc} {diff_sum}")

    ## out put
    # 1 2430
    # 2 2244
    # 3 0
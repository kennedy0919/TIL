T = int(input())

# dr[0] => 상으로 움직였을때r(행)의 변화
# dc[1] => 하 로 움직였을때 c(열)의 변화...
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, 1 + T):
    N, M = map(int, input().split())

    # 2차원 배열로 이루어진 풍선 정보
    arr = [list(map(int, input().split()))for _ in range(N)]

    # 최대값
    max_cnt = 0
    
    # N * M 2차원 배열에서 모든 위치에서 풍선을 터트려보고
    # 상하좌우 확인해서 날리는 종이 꽃가루의 최대값 구하기

    # 행 우선 순회
    for r in range(0, N):
        for c in range(0, M):
            cnt = arr[r][c]
            # 현재 위치는 (r, c)
            # 현재 위치에 있는 풍선의 꽃가루 개수 = arr[r][c]
            # 여기에 상하좌우 풍선도 확인해서 꽃가루 개수
            # 다 더해준 다음에 최대값 구하기
            for d in range(4):
                # d => 방향
                # d = 0 상 d = 1 하 d = 2 좌 d = 3 우
                # 다음 위치(좌표) 계산
                nr = r + dr[d] # 다음 행 좌표 : 현재 행 좌표 + d 방향으로 갔을때 행의 변화량
                nc = c + dc[d] # 다음 열 좌표 : 현재 열 좌표 + d 방향으로 갔을때 열의 변화량

                # 계산한 다음 위치가 2차원 배열의 인덱스 범위 안에 있는지
                if 0 <= nr < N and 0 <= nc < M:
                    # 내가 계산한 위치가 정상적인 위치라면 하고싶은 일 진행
                    # # 풍선안에 있는 꽃가루 개수 세기
                    cnt += arr[nr][nc]

            max_cnt = cnt if cnt > max_cnt else max_cnt

    print(f"#{tc} {max_cnt}")
    # 여기까지 오면 모든 위치 탐색 끝
    # max_cnt에 최대값이 저장되어 있을것이다.
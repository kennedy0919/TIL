T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    field = [list(map(int, input())) for _ in range(0, N)]

    crops = 0

    d = N // 2 
    # 밭의 중앙 좌표
    center = (d, d)

    for r in range(N):
        for c in range(N):
            # 거리 계산 방법
            if abs(r-d) + abs(c-d) <= d:
                crops = crops + field[r][c]

    print(f"#{tc} {crops}")
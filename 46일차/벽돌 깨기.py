# 벽돌 깬 위치 4방향 탐색
# 벽돌로 깬 뒤
# 0 이나 1 이아닌 다른 수를 만나면 그위치에서 다시 깸

"""
1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
"""

def boom(r, c, value):
    # dr = [-1, 1, 0, 0]
    # dc = [0, 0, -1, 1]
    if block[r][c] == 1:
        block[r][c] = 0
        return

    for i in range(1, value):
        dr = [-i, i, 0, 0]
        dc = [0, 0, -i, i]
        for d in range(0, 4):
            nr = r + dr[d] 
            nc = c + dc[d]
            if 0 <= nr < H and 0 <= nc < W:
                if block[nr][nc] == 0:
                    continue

                elif block[nr][nc] == 1:
                    block[nr][nc] = 0

                else:
                    v1 = block[nr][nc]
                    block[nr][nc] = 0
                    boom(nr, nc, v1)
                    
    # block_down()
    return


def block_down():
    for c in range(0, W):
        lst = []
        A = []
        for r in range(0, H):
            lst.append(block[r][c])
        A = sorted(lst)
        # print("A", A)
        # print("+++++++++++++++++++++++")
        # print("lst", lst)
        for r in range(0, H):
            block[r][c] = A[r]


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(0, H)]
    
    boom(1, 2, 1)
    for i in range(0, H):
        print(block[i])
    print("===================")
    boom(2, 2, 3)
    block_down()
    for i in range(0, H):
        print(block[i])
def min_cost(row, sum_num):
    global ans
    # global sum_num

    # 가지치기
    if sum_num > ans:
        return

    if row == N:
        # print("#sum", sum_num)
        if ans > sum_num:
            ans = sum_num
        return
    
    for r in range(0, N):
        can_place = True

        # 세로검사
        for c in range(0, row):
            if visited[c][r] == 1:
                can_place = False
        
        if can_place:
            # sum_num = sum_num + cost[row][r]
            # print("#", row, r)
            visited[row][r] = 1
            min_cost(row+1, sum_num + cost[row][r])
            visited[row][r] = 0
            # sum_num = sum_num - cost[row][r]
            




T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(0, N)]
    ans = 10000
    sum_num = 0
    visited = [[0] * N for _ in range(0, N)]
    min_cost(0, 0)
    print(f"#{tc} {ans}")
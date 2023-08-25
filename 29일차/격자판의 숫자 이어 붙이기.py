T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(0, 4)]
    visited = [([0] * 4) for _ in range(0, 4)]
    stack = []
    string = ""

    visited[0][0] = 1
    stack.append(arr[0][0])
    string = string + str(arr[0][0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(0, 4):
        for c in range(0, 4):
            while stack:
                for d in range(0, 4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < 4 and 0 <= nc < 4 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        stack.append(arr[nr][nc])
                        string = string + str(arr[nr][nc])
                        r, c = nr, nc
                    else:
                        # 머리아픔
    
    
    
    
    
    # for r in range(0, 4):
    #     for c in range(0, 4):
    #         while stack:
    #             for i in range(1, 7):
    #                 for d in range(0, 4):
    #                     nr = r + dr[d]
    #                     nc = c + dc[d]
    #                     if 0 <= nr < 4 and 0 <= nc < 4 and visited[nr][nc] == 0:
    #                         visited[nr][nc] = 1
    #                         stack.append(arr[nr][nc])
    #                         string = string + str(arr[nr][nc])
    #                         print(string)
    #                         r, c = nr, nc
    #                         break
    #                     else:
    #                         if stack:
    #                             break
    #                         else:
    #                             stack.pop()
    #             A = set(string)
    # print(A)

    # for r in range(0, 4):
    #     for c in range(0, 4):
    #             while stack:
    #                 for d in range(0, 4):
    #                     nr = r + dr[d]
    #                     nc = c + dc[d]
                        
    #                 if 0 <= nr < 4 and 0 <= nc < 4 and visited[nr][nc] == 0:
    #                     visited[nr][nc] = 1
    #                     stack.append(arr[nr][nc])
    #                     string= string + str(arr[nr[nc]])


     # while stack:
    #     for r in range(0, 4):
    #         for c in range(0, 4):
    #             for d in range(0, 4):
    #                 nr = r + dr[d]
    #                 nc = c + dc[d]
    #                 if 0 <= nr < 4 and 0 <= nc < 4 and visited[nr][nc] == 0:
    #                     visited[nr][nc] = 1
    #                     stack.append(arr[nr][nc])
    #                     r, c = nr, nc
                

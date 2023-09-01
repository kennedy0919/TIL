"""
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
"""

def solve(n, direction):
    if is_valid(n):
        if arr[n][2] != arr[n+1][6]:
            if direction == 1:
                for i in range(0, 8):
                    if i == 7:
                        C[0] = arr[n][7]
                    else:
                        if arr[n][i] == 1:
                            C[i+1] = 1
                arr[n] = C
                        
        
            else:
                for i in range(0, 8):
                    if i == 0:
                        C[7] = arr[n][0]
                    else:
                        if arr[n][i] == 1:
                            C[i-1] = 1
                arr[n] = C
        else:
            return
    return arr

def is_valid(n):
    return 0 <= n+1 < 4




T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, 4)]
    
    for _ in range(0, K):
        N, direction = map(int, input().split())
        n = N - 1 # 톱니바퀴 인덱스번호
        C = [0] * 8
        A = solve(n, direction)
    print(A)
        # if N == 1:
        #     if arr[n][2] != arr[n+1][6]:
        #         if direction == 1:
        #             for i in range(0, 8):
        #                 if i == 7:
        #                     C[0] = arr[n][7]
        #                 else:
        #                     if arr[n][i] == 1:
        #                         C[i+1] = 1
        #             arr[n] = C
            
        #         else:
        #             for i in range(0, 8):
        #                 if i == 0:
        #                     C[7] = arr[n][0]
        #                 else:
        #                     if arr[n][i] == 1:
        #                         C[i-1] = 1

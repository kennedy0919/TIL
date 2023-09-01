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
# 오늘을 기억할것

def right():
    for i in range(0, 8):
        if i == 7:
            C[n][0] = arr[n][7]
        else:
            if arr[n][i] == 1:
                C[n][i+1] = 1
    

def left():
    for i in range(0, 8):
        if i == 0:
            C[n][7] = arr[n][0]
        else:
            if arr[n][i] == 1:
                C[n][i-1] = 1
    

def solve(n, direction):
    if is_valid(n):
        if n == 3 and arr[n-1][2] != arr[n][6]:
            if direction == 1:
                right()
            else:
                left()

        if arr[n][2] != arr[n+1][6] and visited[n] == 0:
            if direction == 1:
                visited[n] = 1
                right() 
                solve(n+1, -1)
                    
        
            else:
                visited[n] = 1
                left()
                solve(n+1, -1)
        else:
            visited[n] = 1
            
        
    if is_valid2(n):
        if n == 0 and arr[n][2] != arr[n+1][6]:
        
            if direction == 1:
                right()
            else:
                left()
        

        if arr[n][6] != arr[n-1][2] and visited[n] == 0:
            if direction == 1:
                visited[n] = 1
                solve(n-1, -1)
                right()
            else:
                visited[n] = 1
                solve(n-1, 1)
                left()
        else:
            visited[n] = 1
            

    return C



def is_valid(n):
    return 0 <= n+1 < 4

def is_valid2(n):
    return 0 <= n-1 < 4


T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, 4)]
    C = [[0] * 8 for _ in range(0, 4)]

    for _ in range(0, K):
        N, direction = map(int, input().split())
        n = N - 1 # 톱니바퀴 인덱스번호
        visited = [0] * 4
        A = solve(n, direction)
    
    for r in range(0, 4):
        cnt = 0
        for c in range(0, 8):
            if C[r][c] == 0:
                cnt = cnt + 1   
            if cnt == 8:
                C[r] = arr[r] 
        print(cnt)
    
    print(C)
        

    














T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # text = [list(input().split()) for _ in range(0, N)] ?
    text = [input() for _ in range(0, N)]
    arr = [[0] * N for _ in range(0, N)]
    # text = [['....o'], ['...o.'], ['..o..'], ['.o...'], ['o....']]
    for r in range(0, N):
        for c in range(0, N):
            if text[r][c] == ".":
                arr[r][c] = 1

    ans = "NO"
    for r in range(0, N):
        counts = 0
        for c in range(0, N):
            if arr[r][c] == 0:
                counts = counts + 1
            if arr[r][c] == 1:
                counts = 0
            if counts == 5:
                ans = "YES"
                
    for c in range(0, N):
        counts = 0
        for r in range(0, N):
            if arr[r][c] == 0:
                counts = counts + 1
            if arr[r][c] == 1:
                counts = 0
            if counts == 5:
                ans = "YES"
    
    for r in range(0, N):
        for c in range(0, N):
            counts = 0
            for i in range(0, 5):
                if r+i < N and c+i < N:
                    if arr[r+i][c+i] == 0:
                        counts = counts + 1
                    if arr[r+i][c+i] == 1:
                        break
            
                if counts == 5:
                    ans = "YES"
    
    for r in range(0, N):
        for c in range(0, N):
            counts = 0
            for i in range(0, 5):
                if r+i < N and 0 <= c-i < N:
                    if arr[r+i][c-i] == 0:
                        counts = counts + 1
                    if arr[r+i][c-i] == 1:
                        break
            
                if counts == 5:
                    ans = "YES"

    print(f"#{tc} {ans}")
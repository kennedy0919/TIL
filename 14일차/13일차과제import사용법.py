import sys
sys.stdin = open("sum_input.txt", "r")

T = 10

# N = M = 100

for tc in range(1, T + 1):
    t = int(input())

    arr = [list(map(int, input().split())) for _ in range(0, 100)]

    max_r = 0
    for r in range(0, 100):
        sum_r = 0
        for c in range(0, 100): 
            sum_r = sum_r + arr[r][c]

        if max_r < sum_r:
            max_r = sum_r

    # max_r = 0
    for c in range(0, 100):
        sum_c = 0
        for r in range(0, 100):
             sum_c = sum_c + arr[r][c]
                

        if max_r < sum_c:
            max_r = sum_c 

    sum_rc = 0
    for r in range(0, 100):
        for c in range(0, 100):
            if r == c:
                sum_rc = sum_rc + arr[r][c]

    if max_r < sum_rc:
        max_r = sum_rc

    re_sum_rc = 0
    for i in range(0, 100):       
        re_sum_rc = re_sum_rc + arr[99-i][0+i]
    
    if max_r < re_sum_rc:
        max_r = re_sum_rc

    print(f"#{tc} {max_r}")
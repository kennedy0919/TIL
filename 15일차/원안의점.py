T = int(input())

for tc in range(1, 1 + T):
    N = int(input())  # 반지름 길이
    
    counts = 0
    for x in range(0, N + 1):
        for y in range(0, N + 1):
            if (x ** 2) + (y ** 2) <= N ** 2: # 다음식을 만족하면
                counts = counts + 1           # 카운트 해준다
    
    ans = (4 * counts) - (4 * N) - 3  # 원이므로 4번곱해서 구하는데
                                      # 겹치는 부분을 빼준다
    print(f"#{tc} {ans}")
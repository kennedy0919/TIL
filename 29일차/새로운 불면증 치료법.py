T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    sheep_count = []
    j = 1
    cnt = 0
    while True:
        C = N * j
        A = str(C)
        cnt = cnt + 1
        for i in A:
            sheep_count.append(i)

        j = j + 1
        B = set(sheep_count)
                  
        if len(B) == 10:
            break
        
    print(f"#{tc} {cnt * N}")
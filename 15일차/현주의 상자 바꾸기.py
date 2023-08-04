T = int(input())

for tc in range(1, 1 + T):
    N , Q = map(int, input().split())
    box = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
       
        for j in range(L - 1, R):
            box[j] = i

    
    # print(f"#{tc} {(box)}")
    print(f"#{tc}", end = ' ')
    for x in range(0, N):
        print(box[x], end = " ")
    print()

        
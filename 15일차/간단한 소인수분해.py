T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
        
    for num in (2, 3, 5, 7, 11):
        counts = 0
        while N % 1 != 1:
            if N // num == 0:
                counts = counts + 1

        if num == 2:
            a = counts

        if num == 3:
            b = counts

        if num == 5:
            c = counts

        if num == 7:
            d = counts

        if num == 11:
            e = counts

    print(f"#{tc} {a} {b} {c} {d} {e}")
    
    
    # a, b, c, d, e = 0, 0, 0, 0, 0
    # for a in range(0, 100):
    #     for b in range(0, 100):
    #         for c in range(0, 100):
    #             for d in range(0, 100):
    #                 for e in range(0, 100):
        
    #                     if N == (2 ** a) * (3 ** b) * (5 ** c) * (7 ** d) * (11 ** e):
    #                         print(f"#{tc} {a} {b} {c} {d} {e}")
    
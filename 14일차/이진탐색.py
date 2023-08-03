T = int(input())


def book_page_search(P, N):
    l = 1
    r = P
    counts = 0
    while l <= r:
        c = int((l+r) / 2)
        if c < N:
            l = c
            counts = counts + 1
        elif c > N:
            r = c
            counts = counts + 1
        else:
            return counts 
    return 

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    counts_A = book_page_search(P, A)
    counts_B = book_page_search(P, B)
    if counts_A < counts_B:
        print(f"#{tc} B")
    
    elif counts_A > counts_B:
        print(f"#{tc} A")

    else:
        print(f"#{tc} 0")
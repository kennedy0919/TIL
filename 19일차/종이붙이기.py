
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = N/10
    ans = 0
    # if N % 2 == 0:
    #     ans = 3
    #     while N == 2:
    #         ans = ans * (N - 1) * 3
    #         N = N - 2
    
    # if N % 2 == 1:
    #     ans = 5
    #     while N == 2:
    #         for i in range(N, 0, -1):
    #             if i % 2 == 1:
    #                 ans = ans * (i-1) * 3
    # print(ans)
    if (A) % 2 == 0:
        ans = 3 * A + 

    if (A) % 2 == 1:
        ans = 3 ** ((A) - 2) + 2
    print(ans)
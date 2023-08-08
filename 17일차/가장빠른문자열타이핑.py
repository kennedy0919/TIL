T = int(input())

for tc in range(1, 1 + T):
    A, B = input().split()
    # A, B = list(map(str, input().split()))
    counts = 0
    ans_counts = 0

    for i in range(0, len(A) - len(B) + 1):
        for j in range(0, len(B)):
            if B[j] == A[i+j]:
                counts = counts + 1
    
            if B[j] != A[i+j]:
                break
            # if j == len(B)-1  and i == len(A) - len(B):
            # if i == len(A) - len(B) and j == len(B)-1:
            #     for k in range(0, len(B)):
            #         if B[k] == A[i+k]:
            #             counts = counts + len(B)
            for k in range(0, len(B)):
                if A[i+k] == B[j+k]:
                    counts = counts - 1

            if counts == len(B):
                counts = 0
                ans_counts = ans_counts + 1


    # for i in range(0, len(A) - len(B) + 1):
    #     for j in range(0, len(B)):
    #         B[j] == A[i+j]
    #         break  
    #     else:
    #         counts = counts + 1

    # ans = len(A) - (len(B) * counts) + counts


    # ans = len(A) - (len(B) - 1) * ans_counts
    ans = len(A) - (len(B) * ans_counts) + ans_counts

    print(f"#{tc} {ans}")
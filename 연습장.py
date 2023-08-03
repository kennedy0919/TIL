T = int(input())



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    n = len(A)
    counts = 0
    
    for i in range(1<<n):
        sum_i = 0
        counts_i = 0
        for j in range(n):
            
            if i & (1<<j):
                sum_i = sum_i + A[j]
                counts_i = counts_i + 1                

        if sum_i == K and counts_i == N:
            counts = counts + 1        

            
    print(f"#{tc} {counts}")
 
        


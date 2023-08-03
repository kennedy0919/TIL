# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l  
#                 print(bit)

T = int(input())



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    n = len(A)
    counts = 0
    
    for i in range(1<<n): # 첫번째 박스부터 확인하기
        sum_i = 0         # 2 ** n == 1<<n 인데 이라고 표기하는 이유는  
        counts_i = 0      # 아마도 비트연산을 하고있다고 표현하려고 하는거 같음
        for j in range(n): 
            
            if i & (1<<j):
                sum_i = sum_i + A[j]
                counts_i = counts_i + 1                

        if sum_i == K and counts_i == N:
            counts = counts + 1        

            
    print(f"#{tc} {counts}")

############ 집가서 풀어보기
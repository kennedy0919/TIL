def sum_num(N):
    if N > 0:
        return N % 10 + sum_num(N // 10)
    else:
        return 0


N = int(input())
print(sum_num(N))































# def sum_num(num):
#     if num >= 1:
#         return num % 10 + sum_num(num // 10)
    
#     else:
#         return 0

# N = int(input())

# print(sum_num(N))
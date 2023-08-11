# T = 10

# for tc in range(1, T + 1):
#     len_N, N = map(int, input().split())
#     list_N = list(str(N))
#     top = -1
#     size = 100
#     stack = [0] * size
#     top = top + 1
    
#     for i in range(0, len_N):
#         if top != -1 and stack[top] == list_N[i]:
#             top = top -1
#         else:
#             top = top + 1
#             stack[top] = list_N[i]
        

#     print(f"#{tc} {top+1}")

T = 10
for tc in range(1, T + 1):
    str_N, str_num = input().split()
    
    N = int(str_N)
    stack = [0] * N
    top = -1

    for t in str_num:
        if top == -1 or stack[top] != t:  # 스택이 비어있거나, top원소와 다르면 
            top = top + 1
            stack[top] = t
        else:                      # 스택이 비어있지 않고, top과 같으면
            top = top - 1

    ans = "".join(stack[:top+1])
    print(f"#{tc} {ans}")
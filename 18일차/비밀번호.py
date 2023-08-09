T = 10

for tc in range(1, T + 1):
    len_N, N = map(int, input().split())
    list_N = list(str(N))
    top = -1
    size = 100
    stack = [0] * size
    top = top + 1
    
    for i in range(0, len_N):
        if top != -1 and stack[top] == list_N[i]:
            top = top -1
        else:
            top = top + 1
            stack[top] = list_N[i]
        

    print(f"#{tc} {top+1}")
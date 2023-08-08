T = int(input())

for tc in range(1, 1 + T):
    D, A, B = map(int, input().split())
    ans = 0
    for i in range(A, B + 1):
        counts = 0
        real_ans = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counts = counts + 1
            
            if counts == 2:
                ans = ans + counts
            
                list_ans = list(str(ans))

                for i in range(0, len(list_ans)):
                    if list_ans[i] == D:
                        real_ans = real_ans + 1

    print(f"#{tc} {real_ans}")


            


T = int(input())

for tc in range(1, 1 + T):
    N1 = input()
    N2 = input()
    list_N1 = list(N1)
    list_N2 = list(N2)
    ans = 0

    for i in range(0, len(list_N2) - len(list_N1) + 1):
        counts = 0
        if list_N2[i] == list_N1[0]:
            for k in range(1, len(list_N1)):
                if list_N2[i+k] == list_N1[k]:
                    counts = counts + 1

                if list_N2[i+k] != list_N1[k]:
                    break

                if counts == (len(list_N1) - 1):
                    ans = 1

    print(f"#{tc} {ans}")
                
        


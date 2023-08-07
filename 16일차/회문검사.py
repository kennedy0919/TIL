T = int(input())

for tc in range(1, 1 + T):
    N = input()
    latter = list(N)
    M = len(latter) // 2

    for i in range(0, M):
        latter[i], latter[len(latter) - i - 1] = latter[len(latter) - i - 1], latter[i]
        reverse_latter = latter

    if reverse_latter == list(N):
        print(f"#{tc} 1")

    else:
        print(f"#{tc} 0")
T = int(input())

for tc in range(1, 1 + T):
    str1 = list(input())
    str2 = list(input())

    counts = [0] * len(str1)
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if str1[i] == str2[j]:
                counts[i] = counts[i] + 1
    ans = 0
    for i in range(0, len(str1)):
        if ans < counts[i]:
            ans = counts[i]

    print(f"#{tc} {ans}")

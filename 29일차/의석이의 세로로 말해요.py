T = int(input())

for tc in range(1, T + 1):
    text = [input() for _ in range(0, 5)]
    ans = ""
    # ['AABCDD', 'afzz', '09121', 'a8EWg6', 'P5h3kx']
    for i in range(0, 15):
        for j in text:
            if i <= len(j)-1:
                ans = ans + j[i]
                
    print(f"#{tc} {ans}")


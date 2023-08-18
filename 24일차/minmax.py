T = int(input())

for tc in range(1, T +1):
    N = int(input())
    text = list(map(int, input().split()))
    ans = 0
    ans = max(text) - min(text)
    print(f"#{tc} {ans}")
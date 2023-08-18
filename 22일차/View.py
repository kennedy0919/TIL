T = 10

for tc in range(1, T + 1):
    N = int(input())  # N : 건물의 개수
    building = list(map(int, input().split()))
    ans = 0
    
    for i in range(2, N):
        if building[i] - building[i-1] > 0 and building[i] - building[i-2] > 0 and building[i] - building[i+1] > 0 and building[i] - building[i+2] > 0:
            list_building = [building[i-1], building[i-2], building[i+1], building[i+2]]
            ans = ans + building[i] - max(list_building)
        
    print(f"#{tc} {ans}")


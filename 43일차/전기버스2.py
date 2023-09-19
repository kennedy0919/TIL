def min_change(bus_stop, c):
    if bus_stop == N:
        return

    for c in range(0, N):
        if 


T = int(input())

for tc in range(1, T + 1):
    charge = list(map(int, input().split()))
    N = len(charge)
    visited = [0] * N

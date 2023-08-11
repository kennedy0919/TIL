"""
1
3 3
0 1 0
0 1 0
0 1 0
"""

# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(0, N)]
#     ans = 0

#     ans1 = 0
#     for r in range(0, N):
#         counts = 0
#         ans_counts = 0
#         for c in range(0, M):
#             if arr[r][c] == 1:
#                 counts = counts + 1
                
#             if arr[r][c] == 0:
#                 ans_counts = ans_counts + counts
#                 counts = 0
#                 if ans1 < ans_counts:
#                     ans1 = ans_counts
#     print(ans1)
#     ans2 = 0
#     for c in range(0, M):
#         counts = 0
#         ans_counts = 0
#         for r in range(0, N):
#             if arr[r][c] == 1:
#                 counts = counts + 1
                
#             if arr[r][c] == 0:
#                 ans_counts = ans_counts + counts
#                 counts = 0
#                 if ans2 < ans_counts:
#                     ans2 = ans_counts
#     print(ans2)       
#     if ans1 > ans2:
#         ans = ans1
#     elif ans1 < ans2:
#         ans = ans2
#     else:
#         ans = ans1
#     print(f"#{tc} {ans}")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    ans = 0
    for r in range(0, N):
        counts = 0
        for c in range(0, M):
            if arr[r][c] == 1:
                 counts = counts + 1
                 ans = max(counts, ans)
            else:
                counts = 0

    for c in range(0, M):
        counts = 0
        for r in range(0, N):
            if arr[r][c] == 1:
                 counts = counts + 1
                 ans = max(counts, ans)
            else:
                counts = 0

    print(f"#{tc} {ans}")
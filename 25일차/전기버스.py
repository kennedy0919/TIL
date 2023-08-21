 




T = int(input())

for tc in range(1, T + 1):
    # K : 한번 충전으로 가는 거리
    # N : 종점
    # M : 충전기 개수
    cnt = 0
    charge = list(map(int, input().split()))

















# T = int(input())

# for tc in range(1, T + 1):
#     # K : 한번 충전으로 가는 거리
#     # N : 종점
#     # M : 충전기 개수
#     K, N, M = map(int, input().split())
#     charge = list(map(int, input().split()))
#     charge_cnt = 0
#     distance_cnt = 0
#     ans = 0
#     cnt = 0
#     return_charge = 0
#     while True:
#         distance_cnt = distance_cnt + K
#         for i in charge:
#             if i == distance_cnt:
#                 cnt = cnt + 1
#                 break
#             else:
#                 for k in range(1, N):
#                     for j in range(0, M):
#                         if charge[j] == distance_cnt - k:
#                             return_charge = charge[j]
#                             cnt = cnt + 1
#                             break
                    
#                         if distance_cnt - j <= 0:
#                             cnt = 0
#                             break
#                     if return_charge == charge[j]:
#                         break

#                     if cnt == 0:
#                         break
#         if cnt == 0:
#             break            
                        
#         if distance_cnt >= N:
#             ans = cnt
#             break
#     print(f"#{tc} {ans}")

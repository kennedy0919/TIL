def is_triple(lst):
    return lst[0] == lst[1] and lst[1] == lst[2]


def is_run(lst):
    return lst[0] == lst[1] - 1 and lst[1] == lst[2] - 1


# idx 에 놓을 숫자 찾아서 놓기
def baby_gin(idx, used, lst):
    # 종료 조건 : 6개 숫자 자리를 다 정해줌 ( 순열 완성 )
    if idx == 6:
        # 베이비진 검사
        앞 = [lst[i] for i in used[:3]]
        뒤 = [lst[i] for i in used[3:]]
        if (is_run(앞) or is_triple(앞)) and (is_triple(뒤) or is_run(뒤)):
            print(f"베이비진!! {앞} {뒤}")
        return

    # 6개 숫자중에 하나 골라서 idx 위치에 놓기 (이전에 고른거 빼고)
    for i in range(6):
        if i not in used:
            used.append(i)
            baby_gin(idx + 1, used, lst)
            used.pop()


baby_gin(0, [], [1, 2, 4, 7, 8, 3])
baby_gin(0, [], [6, 6, 7, 7, 6, 7])
baby_gin(0, [], [0, 5, 4, 0, 6, 0])
baby_gin(0, [], [1, 0, 1, 1, 2, 3])







# def f(i, N, K):   # N개에서 K개를 고르는 순열
    
#     if i == K:    # 순열 완성: K개를 모두 고른 경우
#         cnt = cnt + 1
#         print(cnt, p)
#         return
#     else:          # p[i]에 들어갈 숫자를 결정
#         for j in range(0, N):
#             if used[j] == 0:    # 아직 사용되기 전이면
#                 p[i] = gin[j]
#                 used[j] = 1
#                 f(i+1, N, K)
#                 used[j] = 0

# gin = [1,2,3,4,5,6]
# N = 6   # N개의 숫자에서
# K = 6   # K개를 골라 만드는 순열
# used = [0] * N  # 이미 사용한 카드인지 표시
# p = [0] * 6
# cnt = 0 
# gen = f(0, N, K)
# count = 0
# ans = 0

# if gen[0] == gen[1] and gen[0] == gen[2]:
#     count = count + 1

# if gen[0] + 1 == gen[1] and gen[0] + 2 == gen[2]:
#     count = count + 1

# if count == 2:
#     ans = ans + 1


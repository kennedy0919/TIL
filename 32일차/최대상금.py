"""
1
2737 1
"""


def swap(cnt):
    global max_v
    # 종료 조건 : 교환 횟수를 다 소모 했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대 상금 계산
    if cnt == N:
        st1 = ""
        for i in range(0, len(S)):
            st1 = st1 + S[i]

        if max_v < int(st1):
            max_v = int(st1)
        return

    # 자리를 바꿀 위치 2개를 교환 한번 할때 마다 새로 지정해줘야 된다
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용
    # 바꿀 위치중에 앞쪽 : i
    # 바꿀 위치중에 뒤쪽 : j
    for i in range(0, len(S) - 1):
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j], S[i]
            # print(S)
            swap(cnt + 1)
            # 바꿨던거 원상 복구 시키고 새로운 i, j 지정
            S[i], S[j] = S[j], S[i]


T = int(input())

for tc in range(1, T + 1):
    S, N = input().split()
    S = list(S)
    N = int(N)
    max_v = 0
    swap(0)
    print(f"#{tc} {max_v}")

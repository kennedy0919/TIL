### 바이너리 카운팅을 통한 사전적 순서
# 부분집합을 생성하기 위한 가장 자연스러운 방법이다.
# 바이너리 카운팅은 사전적 순서로 생성하기 위한 
# 가장 간단한 방법이다.

a = [3,6,7,1,5,4]
N = 6

# for i in range(1, (1 << N)-1):
for i in range(1, 1 << N-1): # (1, 1 << N-1) == (1, (1 << N) // 2)
    group1 = []
    gruop2 = []
    total1 = 0
    total2 = 0

    for j in range(0, N):
        if i & (1 << j):    # j번 비트가 0 이 아니면
            group1.append(a[j])
            total1 = total1 + 1
        else:
            gruop2.append(a[j])
            total2 = total2 + 1
    # r1 = f(group1)
    # r2 = f(gruop2)
    # if r1 and r2:
    #     if min_v > abs(total1-total2):
    print(group1, gruop2)


    
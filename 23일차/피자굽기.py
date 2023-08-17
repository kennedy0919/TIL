T = int(input())

for tc in range(1, T+1):
    # N은 오븐 크기, M 은 피자 개수
    N, M = map(int, input().split())

    # 우리가 구워야할 피자들의 치즈 정보
    pizza_list = list(map(int, input().split()))

    # 다음에 꺼내올 피자 인덱스
    next_i = 0

    # 오븐을 큐로 만들어보자
    oven = [0] * 1000
    ofront = orear = -1

    # 오븐의 크기만큼 피자 넣어주기
    for i in range(N):
        # 오븐에 피자 넣기
        orear += 1
        # 나중에 꺼낼때를 위해서 피자 번호도 같이 넣기
        oven[orear] = [i, pizza_list[i]] # [피자 번호, 치즈 양]
        next_i += 1

    # 오븐에 남아있는 피자의 개수
    remain = N
    # 마지막에 꺼낸 피자의 번호
    last_idx = -1
    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 하나 꺼내서
        ofront = ofront + 1
        pizza_idx, pizza = oven[ofront]
        # 치즈를 녹이고 c // 2
        pizza = pizza // 2
        # 남은 치즈 양이 0이 아니다 ==> 다시 오븐에 넣기
        if pizza != 0 :
            orear = orear + 1
            oven[orear] = [pizza_idx, pizza]
        # 남은 치즈 양이 0이 되었다
        else:
            # 현재 오븐의 자리에 남은피자 하나 꺼내서 넣기
            if next_i < m:
                orear = orear + 1
                oven[orear] = [next_i, pizza_list[next_i]]
                next_i = next_i + 1

            # 넣을 피자가 없다
            else:
                remain = remain - 1   
                # 오븐에 남은 피자도 없는 상황이 온다
                if remain == 0:
                # 현재 피자의 번호가 답이 된다.
                    last_idx = pizza_idx
                # 답을 구하고
                # 반복 종료

    print(f"#{tc} {last_idx + 1}")























# def enq(data):
#     global rear
#     global front
#     if (front + 1) % cQsize == front:
#         front = (front + 1) % cQsize
#     rear = (rear + 1) % cQsize
#     cQ[rear] = data


# def deq():
#     global front
#     front = (front + 1) % cQsize
#     return cQ[front] // 2

# def pizza():
#     for i in text:
#         enq(i)
#     for i in range(0, 20):



# T = int(input())

# for tc in range(1, T +1):
#     N, M = map(int, input().split())
#     text = list(map(int, input().split()))
#     cQsize = N
#     cQ = [0] * cQsize
#     front = 0
#     rear = 0
#     cnt = 0
#     ans = 0
    
#     for i in text:
#         enq(i)
    


    # while True:
    #     if deq() == 0:
    #         cnt = cnt + 1
    #         break
    #     else:
    #         for _ in range(0, 100):
    #             cnt = cnt + 1
    #             deq()
    
    # ans = cnt % M
    # print(f"#{tc} {ans}")


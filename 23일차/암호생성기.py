T = 10

for i in range(1, T + 1):
    tc = int(input())
    code = list(map(int, input().split()))
    size = 100000
    q = [0] * size
    front = rear = -1
    ans = []

    for i in range(0, 8):
        rear = rear + 1
        q[rear] = code[i]
    while True:
        for i in range(1, 6):
            front = front + 1
            rear = rear + 1
            q[rear] = q[front] - i

            if q[rear] <= 0:
                q[rear] = 0
                break
        if q[rear] == 0:
            break
    # for i in range(0, 8):
    #     ans.append(q[front+i+1])#ans + [1]
    # for i in ans:
    #     print(f"#{tc} {(i, end = '')}")
    print(f"#{tc} {q[rear-7]} {q[rear-6]} {q[rear-5]} {q[rear-4]} {q[rear-3]} {q[rear-2]} {q[rear-1]} {q[rear]}")
    


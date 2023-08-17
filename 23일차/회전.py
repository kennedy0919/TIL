# def enqueue(item):
#     global rear
#     if isFull():
#         return
#     rear = rear + 1
#     q[rear] = item

# def dequeue():
#     global front
#     if isEmpty():
#         return
#     front = front + 1
#     return q[front]

# def isFull():
#     return rear == size -1

# def isEmpty():
#     return front == rear



# T= int(input())

# for tc in range(1, T +1):
#     N, M = map(int, input().split())
#     text = list(map(int, input().split()))
#     size = N
#     q = [0] * size 
#     front = rear = -1
#     ans = 0
    
#     for i in range(0, M):
def enq(data):
    global rear
    global front
    if (front + 1) % cQsize == front:
        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data


def deq():
    global front
    front = (front + 1) % cQsize
    return cQ[front]
T = int(input())

for tc in range(1, T +1):
    N, M = map(int, input().split())
    text = list(map(int, input().split()))
    cQsize = N
    cQ = [0] * cQsize 
    front = 0
    rear = 0
    for i in text:
        enq(i)
    for _ in range(0, M):
        deq()
    print(f"#{tc} {deq()}")


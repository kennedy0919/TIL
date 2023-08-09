T = int(input())

for tc in range(1, 1 + T):
    text = input()
    # stack = []
    # for i in N:
    #     stack.append(i)
    #     if stack[i] == stack[i+1]:
    #         stack.pop[i], stack.pop[i+1]
    
    # ans = len(stack)
    # print(f"#{tc} {ans}")

    # 스택을 이용해서 풀껀대 
    # 일단 문자를 스택에 넣어(맨 처음 글자는 넣음)
    # 두번째 글자부터는 내가 제일 최근에 넣었던 글자와 비교해서
    # 만약 같다면 스택에서 pop
    # 다르다면 현재 글자를 스택에 push
    size = 1000
    stack = [0] * size
    top = -1

    top = top + 1
    stack[top] = text[0]

    for i in range(1, len(text)):
        if top != -1 and stack[top] == text[i]:
            top = top -1

        else:
            top = top + 1
            stack[top] = text[i]

    print(f"#{tc} {top+1}") #top 은 마지막 인덱스 그래서 거기서 +1 한게 리스트 길이



################################################################
T = int(input())

for tc in range(1, 1 + T):
    text = input()
    top = -1
    size = 1000
    stack = [0] * size
    top = top + 1
    stack[top] = text[0]

    for i in range(1, len(text)):

        if top != -1 and stack[top] == text[i]:
            top = top - 1

        else:
            top = top + 1
            stack[top] = text[i]

    print(f"#{tc} {top+1}")

#### 밑에가 내가푼거




















# def sss(N):
#     for i in range(0, len(N) - 1):
#             if N[i] == N[i+1]:
#                 N.pop(i), N.pop(i+1)
#                 return N

# for tc in range(1, 1 + T):
#     N = list(input())
#     counts = 0
#     for _ in range(0, len(N) - 1):
#         for i in range(0, len(N) - 1):
#             if N[i] == N[i+1]:
#                 N.pop(i), N.pop(i+1)
                
#                 counts = counts + 2
#     ans = len(N) - counts
#     print(f"#{tc} {ans}")

# top = -1
# def my_push(item):
#     global top
#     top = top + 1
#     if top == size:
#         print("오버플로우")
#     else:
#         stack[top] = item

# def my_pop():
#     global top
#     if top == -1:
#         print("언더플로우")
#     else:
#         top = top -1
#         return stack[top+1]

# def peek():
#     if top > -1:
#         return stack[top]
    
# for tc in range(1, 1 + T):
#     N = input()
#     size = len(N)
#     stack = [0] * size

#     for i in N:
#         my_push(i)
#     print(stack)



T = int(input())


# def A_push(item):
#     stack.append(item)   

# def A_pop(item):
#     if len(stack) == 0:
#         return
#     else:
#         return stack.pop()
# top = -1
# size = len(T)
# def my_push(item):
#     global top
#     top = top + 1
#     if top == size:
#         print("오버플로우")

# def my_pop():
#     global top
#     if top == -1:
#         print("언더플로우")
#         return
#     else:
#         top = top - 1
#         return stack[top + 1]



for tc in range(1, 1 + T):
    row = input() # 괄호의 짝이 맞는지 검사할 문자열

    stack = [] # 스택

    answer = 1 # 1이면 괄호가 제대로 되어있다, 0이면 제대로 xx

    # 괄호 검사
    # row 에서 한글자씩 떼어 와서 검사
    for c in row:
        if c == "(":
            stack.append(c)

        if c == ")":
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()
            if not (b == "(" and c == ")"):
                answer = 0
                break

    if len(stack) > 0:
            answer = 0

    print(f"#{tc} {answer}")             
    # 떼어낸 한 글자가 만약 여는 괄호다 ? => 스택에 삽입
    # 떼어낸 글자가 닫는 괄호다 => 스택에서 하나 꺼내온 다음에
    # 짝이 맞는지 검사 => 괄호의 종류가 다르면 오류
    # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류!!
    
    # 모든 글자 검사가 끝난 후에 스택이 비어있지 않으면 오류!!
"""
4
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
"""

# def A_push(item):
#     stack.append(item)   

# def A_pop(item):
#     if len(stack) == 0:
#         return
#     else:
#         return stack.pop()
    

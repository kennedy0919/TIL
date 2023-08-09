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


            
                
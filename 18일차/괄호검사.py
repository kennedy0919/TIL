T = int(input())

for tc in range(1, 1 + T):
    row = input()
    stack = []
    answer = 1

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

        if c == "{":
            stack.append(c)

        if c == "}":
            if len(stack) == 0:
                answer = 0
                break
            b = stack.pop()
            if not (b == "{" and c == "}"):
                answer = 0
                break

        if c == "[":
            stack.append(c)

        if c == "]":
            if len(stack) == 0:
                answer = 0
                break
            b = stack.pop()
            if not (b == "[" and c == "]"):
                answer = 0
                break

    if len(stack) > 0:
        answer = 0
     
    print(f"#{tc} {answer}")



def get_result(postfix):
    stack = []

    for c in postfix:
        if c not in ["+", "-", "/", "*", "."]:
            stack.append(int(c))

        else:
            if c == ".":
                if len(stack) >= 2:
                    return "error"
                else:
                    return stack.pop()
            if len(stack) <= 1:
                return "error"
            right = int(stack.pop())
            left = int(stack.pop())

            if c == "+":
                result = left + right

            if c == "-":
                result = left - right

            if c == "/":
                result = left // right

            if c == "*":
                result = left * right
            
            stack.append(result)
    return

T = int(input())

for tc in range(1, T + 1):
    string = input().split()
    print(f"#{tc}", get_result(string))
            
                    
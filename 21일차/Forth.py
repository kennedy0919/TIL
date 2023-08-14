def get_result(postfix):
    stack = []
    
    for c in postfix:

        if c not in ["+", "-", "/", "*", "."]:
            stack.append(int(c))
        
            print(stack)
        else:
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
    return stack.pop()

T = int(input())

for tc in range(1, T + 1):
    string = input().split()
    print("#", string)
    print(f"#{tc}", get_result(string))
            
                    
T = int(input())

for tc in range(1, T + 1):
    text = input()
    stack = []
    top = -1
    stack.append(text[0])
    top = top + 1

    while stack:
        if 
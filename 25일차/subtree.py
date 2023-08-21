def preorder(t):
    global cnt
    if t != 0:
        cnt = cnt + 1
        preorder(child_left[t])
        preorder(child_right[t])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))

    child_left = [0] * (E + 2)
    child_right = [0] * (E + 2)
    cnt = 0

    for i in range(0, E):
        parent = tree[i*2]
        child = tree[i*2+1]
        
        if child_left[parent] == 0:
            child_left[parent] = child
        else:
            child_right[parent] = child
    # print(child_left)
    # print(child_right)
    preorder(N)
    print(f"#{tc} {cnt}")
    

        
    
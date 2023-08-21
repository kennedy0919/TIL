def postorder(t):
    if t != 0:
       
        postorder(child_left[t])
        
        postorder(child_right[t])
        
        

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    node = range(1, N + 1)
    child_left = [0] * (N + 1)
    child_right = [0] * (N + 1)

    for i in range(0, E):
        parent = node[i*2]
        child = node[i*2+1]
        
        if child_left[parent] == 0:
            child_left[parent] = child
        else:
            child_right[parent] = child
    
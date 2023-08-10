# def dfs(s, V, G):

#     visited = [0] * (V + 1)
#     stack = []

#     i = s # i 는 시작정점
#     visited[i] = 1

#     while True:
#         for j in adj[i]:
#             if visited[j] == 0:
#                 stack.append(i)
#                 visited[j] = 1
#             if stack[i-1] == G:
#                 print(1)    
#         else:
#             if stack:
#                 i = stack.pop()
#             else:
#                 print(0)
#                 break


# T = int(input())

# for tc in range(1, T + 1):

#     V, E = map(int, input().split())
#     adj = [[] for _ in range(0, V + 1)]
#     for i in range(0, E):
#         s, e = map(int, input().split())
#         adj[s].append(e)
#         adj[e].append(s)

#     S, G = map(int, input().split())
#     dfs(S, V, G)

def dfs(S, V, G):
    
    visited = [0] * (V + 1)
    stack = []
    visited[S] = 1
    i = S
    ans = 0
    while True:
        for j in adj[i]:
            if visited[j] == 0:
                stack.append(i)
                i = j
                visited[j] = 1
                if j == G:
                    ans = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
        if ans == 1:
            break

    return ans
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(0, V + 1)]
    for i in range(0, E):
        s, e = map(int, input().split())

        adj[s].append(e)

    S, G = map(int, input().split())
    ans1 = dfs(S, V, G)
    print(f"#{tc} {ans1}")
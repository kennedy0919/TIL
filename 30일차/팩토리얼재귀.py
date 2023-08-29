def factory(N):
    if N > 0:
        return N * factory(N-1)
    else:
        return 1
    
N = int(input())
print(factory(N))
def fibo(i):
    if i >= 2:
        return fibo(i-1) + fibo(i-2)
    else:
        return i

N = int(input())

print(fibo(N))
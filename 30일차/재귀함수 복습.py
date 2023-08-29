def boom(n):
    if n == 0:
        print("boom")
    else:
        print(n)
        n = n - 1
        boom(n)
boom(5)

# 피보나치 수열
A = 0
def pibonacci(i):
    
    if i < 2:
        return i
    else:
        return pibonacci(i-1) + pibonacci(i-2)



for i in range(0, 10):
    print(pibonacci(i), end = " ")

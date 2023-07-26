def solve2070():
    t = int(input())
    for i in range(1, t + 1):
        x,y = map(int, input().split(' '))
        if x > y:
            ans = '>'
        elif x == y:
            ans = '='
        else:
            ans = '<'
 
 
        print(f"#{i} {ans}")
    pass
 
if __name__ == "__main__":
    solve2070()

T = int(input())

n = list(map(int, input().split()))

def solution():
    for i in (1, T + 1):
    
        if n[0] > n[1]:

            print(f"#{i} >")

        elif n[0] == n[1]:

            print(f"#{i} =")

        else:

            print((f"#{i} <"))
    return n

print(solution(n))
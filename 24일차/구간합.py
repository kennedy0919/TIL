# i : i번째 원소
# n : text 길이 
# subsum : 부분집합 합
def subset(i, n, subsum):
    if i == n:


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    text = list(map(int, input().split()))
    selected = [0] * 3
    


# 재귀 함수
def backtracking(i, now_sum):
    # 최소값 수정해야 하니까, global 선언
    
    # 종료 조건
    # i가 몇일때 종료 해야될까?
    # 최소값 비교는 언제 해야할까?

    # 재귀호출
    # 0 ~ n-1 번째 열 중에서 이전에 고른적이 없는 j얄 선택

    # 고른적이 없다면
    # j번째 열을 골랐다고 체크 하고
    # i+1 번째 행에서 몇번째 열을 고를건지 선택하러 ㄱㄱ ㅋ
    # 다시 돌아와서 j번째 열을 고르지 않았다고 원복한 뒤에 다음 열에대한 탐색
    if i == N:
        




T = int(input())

for tc in range(1, T +1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(0, N)]

    # 행을 기준으로 j번째 열에 있는 숫자를 선택했는지 나타내는 배열
    selected = [0] * N
    # 최소값
    min_v = 100
    # min_n = 0 ???? 생각해보기
'''
1
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF

'''

T = int(input())

for tc in range(1, 1 + T):
    # 2차원 배열의 크기 N, 회문의 길이 M
    N, M = map(int, input().split())
    text = [list(input()) for _ in range(N)]

    # 우리가 찾는 회문
    answer = ""

    # 행 우선 순회
    for r in range(0, N):
        for c in range(0, N - M + 1):
            # (r, c) 위치에 있는 글자부터 회문을 만들기 시작
            # 회문의 길이가 m이니까 (r , c) ~ (r, r+M) 까지의 글자를 모아서
            word_row = ""

            for k in range(0, M):
                word_row = word_row + text[r][c+k]

            # word_row 가 회문인지 아닌지 판별(인덱스 판별)
            counts = 0
            for i in range(0, M):
                if word_row[i] == word_row[M-1-i]:
                    counts = counts + 1
                if word_row[i] != word_row[M-1-i]:
                    break
                if counts == (M // 2):
                    answer = word_row
    
    # 열 우선 순회
    for c in range(0, N):
        for r in range(0, N - M + 1):
            # (r, c) 위치에 있는 글자부터 회문을 만들기 시작
            # 회문의 길이가 m이니까 (r , c) ~ (r, r+M) 까지의 글자를 모아서
            word_row = ""

            for k in range(0, M):
                word_row = word_row + text[r+k][c]

            counts = 0
            # word_row 가 회문인지 아닌지 판별(인덱스 판별)
            for i in range(0, M):
                if word_row[i] == word_row[M-1-i]:
                    counts = counts + 1
                if word_row[i] != word_row[M-1-i]:
                    break
                if counts == (M // 2):
                    answer = word_row

    print(f"#{tc} {answer}")
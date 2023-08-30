# now : 현재 방 번호
# e_sum : 현재까지 사용한 배터리 사용량
def patrol(now, e_sum):
    global min_value

    if e_sum >= min_value:
        return

    # 종료 조건
    # 모든 방을 다 방문했으면 시작지점으로 돌아가는 배터리 양 까지 계산
    # 최소값 구하기
    if 0 not in visited:
        min_value = min(min_value, e_sum + e[now][0])
        return

    # now 위치에서 갈 수 있는 다음 방을 선택
    # 선택기준 => 이전에 내가 방문한적이 없는 방
    for next_room in range(n):
        if visited[next_room] == 0 and next_room != now:
            # next_room 은 갈 수 있는 방
            visited[next_room] = 1
            patrol(next_room, e_sum + e[now][next_room])
            visited[next_room] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    e = [list(map(int, input().split())) for _ in range(n)]
    # e[i][j] = i번방에서 j번방으로 가는데 소모하는 배터리 양

    visited = [0] * n
    # 출발시 첫번째 방은 방문했다고 처리
    visited[0] = 1

    min_value = 10000
    patrol(0, 0)

    print(f"#{tc} {min_value}")

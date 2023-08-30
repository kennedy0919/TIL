T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    p1 = []
    p2 = []
    ans = 0

    for i in range(0, 6):
        p1.append(card[i*2])
        p2.append(card[i*2+1])

    C = [0] * 10
    cnt = 0
    run_p1 = 0
    for i in range(0, 6):
        C[p1[i]] = C[p1[i]] + 1
        cnt = cnt + 1
        if C[p1[i]] == 3:
            run_p1 = cnt
            break
    print(cnt)
    cnt = 0
    run_p2 = 0
    for i in range(0, 6):
        C[p2[i]] = C[p2[i]] + 1
        cnt = cnt + 1
        if C[p2[i]] == 3:
            run_p2 = cnt
            break
    print(cnt)
    cnt = 0
    tri_p1 = 0
    for i in range(0, 4):
        cnt = cnt + 1
        if p1[i] + p1[i+2] == p1[i+1]:
            tri_p1 = cnt
            break
    print(cnt)
    cnt = 0
    tri_p2 = 0
    for i in range(0, 4):
        cnt = cnt + 1
        if p2[i] + p2[i+2] == p2[i+1]:
            tri_p2 = cnt
            break
    print(cnt)
    win_run_p1 = 0
    win_run_p2 = 0
    if run_p1 <= run_p2:
        win_run_p1 = run_p1
    else:
        win_run_p2 = run_p2
    
    win_tri_p1 = 0
    win_tri_p2 = 0
    if tri_p1 <= tri_p2:
        win_tri_p1 = tri_p1
    else:
        win_tri_p2 = tri_p2
    
    if win_run_p1 + win_run_p2 < win_tri_p1 + win_tri_p2:
        if win_run_p1 <= win_run_p2:
            ans = 2
        else:
            ans = 1
    
    if win_run_p1 + win_run_p2 > win_tri_p1 + win_tri_p2:
        if win_tri_p1 <= win_tri_p2:
            ans = 2
        else:
            ans = 1

    if run_p1 == 0 and run_p2 == 0 and tri_p1 == 0 and tri_p2 == 0:
        ans = 0
    # if win_run_p1 + win_run_p2 == win_tri_p1 + win_tri_p2:
    #     if win_run_p1 <= win_run_p2:
    #         ans = 1
    #     else:
    #         ans = 2
    
    print(ans)

    
    
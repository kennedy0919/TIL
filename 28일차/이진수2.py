T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    bin_string = ""
    cnt = 0

    while cnt <= 13:
        
        N = N * 2
        
        if N >= 1:
            bin_string = bin_string + "1"
            
        else:
            bin_string = bin_string + "0"



        cnt = cnt + 1
        if N == 0:
            break
    if cnt == 14:
        bin_string = "overflow"
    print(f"#{tc} {bin_string}")


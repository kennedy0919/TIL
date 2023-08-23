T = int(input())

for tc in range(1, T + 1):
    N, text = input().split()
    print(f"#{tc}", end = " ")
    # for i in range(0, 4):
    #     if text[i].isdigit():
    #         print(bin(text[i]), end = " ")
        
    #     else:
    for i in range(0, int(N)):
        bit = [0] * 4
        bit4 = "0x" + text[i:i+1]
        dec = int(bit4, 16)
        
        
        if dec - 8 >= 0:
            bit[0] = 1
            dec = dec - 8
        if dec - 4 >= 0:
            bit[1] = 1
            dec = dec - 4
        if dec - 2 >= 0:
            bit[2] = 1
            dec = dec - 2
        if dec - 1 == 0:
            bit[3] = 1
        for j in range(0, 4):
            print(bit[j], end = "")
        
    print()
        
    
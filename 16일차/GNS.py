T = int(input())

for i in range(1, 1 + T):
    tc, len_tc =input().split()
    len_tc = int(len_tc)
    N = list(map(str, input().split()))
    counts = [0] * 10

    for i in range(0, len_tc):
        
        num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
        for k in range(0, 10):
            if N[i] == num_list[k]:
                counts[k] = counts[k] + 1
           
    ans = " "
    for i in range(0, 10):
            ans =  ans + (num_list[i] + " ") * counts[i]

    print(f"{tc} {ans}")


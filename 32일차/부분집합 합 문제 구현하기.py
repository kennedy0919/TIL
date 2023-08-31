lst = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(lst)
print(sum(lst))
cnt = 0
# subset = []  잘못된 방법

def comb(idx, r, selected):
    global cnt
    # global subset   잘못된 방법

    if idx == N:
        # subset = [lst[i] for i in selected]
        subset = []
        for i in selected:
            subset.append(lst[i])
            
        if sum(subset) == 0:
            cnt = cnt + 1
            print(subset)
        return
    
    selected.append(idx)
    comb(idx+1, r+1, selected)

    selected.pop()
    comb(idx + 1, r, selected)

comb(0,0,[])
print(cnt)
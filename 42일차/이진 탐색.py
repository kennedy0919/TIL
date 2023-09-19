def binarySearch_left(low, high, target):
    # if low > high:
    #     return 0

    mid = (low + high) // 2
    if target == A[mid]:
        return 1

    elif target < A[mid]:
        return binarySearch_right(low, mid-1, target)
    
    else:
        return 0

def binarySearch_right(low, high, target):
    # if low > high:
    #     return 0

    mid = (low + high) // 2
    if target == A[mid]:
        return 1

    elif target > A[mid]:
        return binarySearch_left(mid+1, high, target)

    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    B = sorted(B)
    low = 0
    high = len(A)-1
    ans = 0
    mid = (low + high) // 2
    for i in B:
        if i < A[mid]:
            ans = ans + binarySearch_left(0, len(A)-1, i)
        elif i > A[mid]:
            ans = ans + binarySearch_right(0, len(A)-1, i)
        else:
            ans = ans + 1
        

    print(f"#{tc} {ans}")
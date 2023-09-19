def merge(left, right):
    result = []  

    while len(left) > 0 or len(right) > 0:

        if len(left) > 0 and len(right) > 0:
           
            if left[0] <= right[0]:
                result.append(left.pop(0))
           
            else:
                result.append(right.pop(0))
        
        elif len(left) > 0:
            result.append(left.pop(0))
        
        elif len(right) > 0:
            result.append(right.pop(0))

    return result



def mergeSort(lst):
    global cnt
    m = len(lst)

    if m == 1:
        return lst

    mid = m // 2
    left, right = lst[:mid], lst[mid:]
    if left[mid-1] > right[mid-1]:
        cnt = cnt + 1
    left = mergeSort(left)  
    right = mergeSort(right)  

    return merge(left, right)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    print(mergeSort(num))
    print(cnt)

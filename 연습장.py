def merge(left, right):
    result = []  
    cnt_l = 0
    cnt_r = 0
    while cnt_l < len(left) or cnt_r < len(right):

        if cnt_l < len(left) and cnt_r < len(right):
           
            if left[cnt_l] <= right[cnt_r]:
                result.append(left[cnt_l])
                cnt_l = cnt_l + 1
            else:
                result.append(right[cnt_r])
                cnt_r = cnt_r + 1
        
        elif cnt_l < len(left):
            result.append(left[cnt_l])
            cnt_l = cnt_l + 1

        elif cnt_r < len(right):
            result.append(right[cnt_r])
            cnt_r = cnt_r + 1

    return result



def mergeSort(lst):
    global cnt
    m = len(lst)

    if m == 1:
        return lst

    mid = m // 2
    left, right = lst[:mid], lst[mid:]
    if mid % 2 == 0:
        if left[mid-1] > right[mid-1]:
            cnt = cnt + 1
    else:
        if left[mid-1] > right[mid]:
            cnt = cnt + 1
    left = mergeSort(left)  
    right = mergeSort(right)  

    return merge(left, right)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    print(mergeSort(num)[len(num) // 2])
    print(cnt)

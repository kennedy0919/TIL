# selection_sort(i):  i 번째 자리에 놓을 리스트에서 i번째로 작은 원소 찾기
# 리스트의 길이가 5 라면??
# selection_sort(0) : 0번 인덱스에 제일 작은 원소 놓기
# selection_sort(1) : 1번 인덱스에 그 다음을 작은 원소를 놓기
# selection_sort(2) : 2번 인덱스에
# selection_sort(3) : 3번 인덱스에
# selection_sort(4) : 4번 인덱스에
# selection_sort(5) : 5번 인덱스는 범위를 벗어나니까 종료
# 종료 조건 // 재귀 호출

def selection_sort(i, lst):
    if i == len(lst):  # 종료조건
        return 
    min_i = i
    for j in range(i+1, len(lst)):
        if lst[min_i] > lst[j]:
            # 내가 알고있던 최소값보다 j번째 위치의 원소가 작다
            min_i = j
    # 자리바꾸기
    lst[i], lst[min_i] = lst[min_i], lst[i]    # 제일 작은 값 찾아서 i번 인덱스에 놓기(자리교환)

    selection_sort(i+1, lst)   # 재귀호출 (i+1) 번 인덱스에 놓을 작은 원소 찾으러 ㄱㄱ
               
        
        
                        
                    


lst = [3,2,4,5,1,7,6]

selection_sort(0, lst)

print(lst)

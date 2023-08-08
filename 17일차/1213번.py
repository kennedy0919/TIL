T = 10

for i in range(1, 1 + T):
    tc = int(input())
    A = input()
    list_A = list(A)
    text = input()
    list_text = list(text)
    ans_counts = 0

    for i in range(0, len(list_text) - len(list_A) + 1):
        counts = 0
        if list_text[i] == list_A[0]:
            for k in range(1, len(list_A)):
                if list_text[i+k] == list_A[k]:
                    counts = counts + 1
                if list_text[i+k] != list_A[k]:
                    break
                
                if counts == (len(list_A) - 1):
                    ans_counts = ans_counts + 1
    
    print(f"#{tc} {ans_counts}")
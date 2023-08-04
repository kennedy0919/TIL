T = int(input())

for tc in range(1, 1 + T):
    D, A, B, F = map(int, input().split())

   
    # 파리가 움직인 시간이 t 라면 D = (A + B)t 이 성립해야함
    t = D / (A + B)
    ans = F * t


    print(f"#{tc} {ans}")
    
    
    
    
    
    




                
            
         

        




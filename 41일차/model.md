# model class에 변경사항이 생겼다면
1. model class 변경
2. makemigrations
3. migrate 
   
  

# Model Field
1. CharField : 문자열 필드 max_lengthr가 필수인자 (길이제한 있음)
2. TextField() : 글자의 수가 많을 때 사용
3. DateTimeField : 선택인자   
  1. auto_now : 데이터가 저장될 떄마다 자동을 현재 날짜시간을 저장
  2. auto_now_add : 데이터가 처음 생성될 떄만 자동으로 현재 날짜시간을 저장


# Admin site
#### 관리자 계정 만들기
- commend : python manage.py createsuperuser

#### models.py
- models.py 에 변화가 생기면 반드시 다음 커맨드를 입력!!!
- python manage.py makemigrations
- python manage.py migrate
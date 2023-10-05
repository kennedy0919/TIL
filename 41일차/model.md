
### get함수는 url에 추가

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





# 처음부터
1. 위에꺼 다하고(pip install 하고 freeze 까지) settings 건들기
2. models.py 만들어 주기
  - models.py 변경사항있으면 makemogrations 랑 migrate 하기

3. project url 에 있는 곳에 include 해주고 url 추가
4. app url 에 있는곳에 url 추가 해주기
5. views.py 에 가서 함수 만들어주기
6. tamplates 에서 파일 만들고 조작하기


#### 이미지 넣고싶을때
1. static 폴더 만들기
넣을 html 폴더 extends 밑에 load static 태그 넣기 
2. img 태그 넣기 (src 에 이미지경로 넣기)
3. models.py 에 image = models.ImageField(blank=True) 넣기
  - blank=True 가 의미하는것은 공백을 허용하겠다
4. Pillow 라이브러리 설치하기
5. app에 forms.py 만들기
6. html 에 가서 받을수있게 다시 수정해주기


#### 글 작성하고 싶을때
1. app url 에 추가해주기
2. views.py 에 함수 추가해주기
3. tamplates에 html 추가해주기(create으로 많이쓰는듯)
4. 추가한 곳에 내용 작성해주기
5. index에 articles:create url 추가해주기

#### 하 머가이리많아



# 로그인 세션 만들고 싶으면
1. accoutns/urls.py 만들고
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    
]
작성해주기

2. crud/urls.py 에 
path('accounts/', include('accounts.urls')),
작성해주기

3. settings.py 에
'accounts', 추가해주기

4. accounts/models.py 에
from django.contrib.auth.models import AbstractUser
추가해주기

5. settings.py 맨 아래에
AUTH_USER_MODEL = 'accounts.User'
추가해주기

6. accounts/admin.py 에
from django.contrib.auth.admin import UserAdmin
from.models import User

admin.site.register(User, UserAdmin)
추가해주기

- !!!!주의!!!!
- 프로젝트 중간에 AUTH_USER_MODEL을 변경할수 없음
- 만약 이미 프로젝트가 진행되고 있다면 데이터베이스 초기화후 진행할것

7. accounts/urls.py 에
path('login/', views.login, name='login'),
추가해주기

8. accounts/login.html 에
<h1>로그인</h1>
<form action="{% url "accounts:login" %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
추가해주기

9. account/views.py 에
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == "POST":
        pass
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
추가해주기

10. accounts/views.py 에
import redirect 해주고
from django.contrib.auth import login as auth_login
추가해주고
pass 부분
form = AuthenticationForm(request, request.POST)
  if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('articles:index')
으로 바꿔주기

11. articles/index.html 에
<a href="{% url "accounts:login" %}">Login</a>
추가해주기

12. makemigrations 랑 migrate 해주기


# 로그아웃 하고 싶으면

1. accounts/urls.py 에
path('logout/', views.logout, name='logout'),
추가해주기

2. articles/index.html 에
<form action="{% url "accounts:logout" %}" method="POST">
    {% csrf_token %}
    <input type="submit" value='Logout'>
추가하기

3. accounts/views.py 애
from django.contrib.auth import logout as auth_logout
랑
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

추가해주기

4. 

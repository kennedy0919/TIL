## "y" : 다시 코드모드로 변경
## "m" : 쉘 하나가 마크다운 모드로 변경
## "a" : 커서 기준 위에 쉘 하나 추가
## "b": 커서 기준 아래에 쉘 하나 추가
## "dd" 쉘 삭제
## "shift + enter" : 실행 후 커서를 아래로 이동
## " ctrl + enter" : 싱행 후 커서를 제자리에

API_KEY = "5ec480eef0fc2ce16b81fae0971f6d58"
lat = 37.56
lon = 126.97
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
import requests
response = requests.get(url).json()
# 서울의 위도 경도를 활용해서 데이터를 받아왔다.
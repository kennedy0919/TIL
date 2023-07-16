'''
import random

gamecode = ["가위", "바위", "보"]

print(random.choice(gamecode))

user = input("컴퓨터와 가위바위보 하세요")

com = random.choice(gamecode)

if user == com :
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 비겼습니다.")

elif user == "가위" and com == "바위":
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 졌습니다.")

elif user == "바위" and com == "보":
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 졌습니다.")

elif user == "가위" and com == "보":
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 이겼습니다.")

elif user == "바위" and com == "가위":
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 이겼습니다.")

elif user == "보" and com == "바위":
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 이겼습니다.")

elif user == "보" and com == "가위":
    print("유저가", user,"를 내고","컴퓨터가", com,"을 내서 졌습니다.")
'''
A,B = map(int, input().split())
if (A !=2) and (B !=2):
    if A == 1:
        print("A")
    else :
        print("B")    

else :
    if A > B :
        print("A")
    else :
        print("B")

# map(함수, 리스트)
# lambda(매개변수, 함수)
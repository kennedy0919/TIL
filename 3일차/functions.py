# def greeting(name, age):
#     print(f"안녕, {name}, {age}!!")


# greeting("엘리스", 25)

# print("hi", "aaa", "bbb", "ccc")
# numbers = [1, 2, 3]
# result = map(str, numbers)

# print(result)


# import sys
# sys.stdin = open("input.text")

############### map + lambda#################
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x:x * 2, numbers))
print(result)

# 세제곱 함수
# 입력받은 수를 세제곱하여 반환(return)하는 함수 cube()를 만들어 보세요.

def cube(x):
    return x * x * x
print(cube(2))

def area(h , w):
    return h * w

print(area(30,20))

#### filter(함수, 반복가능한)
    
    
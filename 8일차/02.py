# # 인스턴스.매서드()
# "abc".upper()

# # 클래스.메서드(인스턴스 자기자신)
# str.upper("abc")

# ##### 위에 두개는 똑같은 거
# ##### 위가 아래의 축약형


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __gt__(self, other):
        return self.width * self.height > other.width * other.height
    
    def __eq__(self, other):
        return self.width * self.height == other.width * other.height
    

s1 = Shape(3, 4)
s2 = Shape(5, 6)
s3 = Shape(6, 5)
print(s2 > s1)
print(s2 == s1)

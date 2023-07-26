class Coffee:
    
    company = "Starbugs"

    def __init__(self, name):
        self.name = name

    
    def ice(self):
        return f"{self.name}을 차갑게 준비합니다."
    
    def hot(self):
        return f"{self.name}을 따뜻하게 준비합니다"
    
coffee1 = Coffee("Americano")
coffee2 = Coffee("capuccino")
coffee3 = Coffee("cafe latte")

print(coffee1.ice())

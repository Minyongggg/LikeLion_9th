class Calculator:
    def __init__(self, name, age):
        self.result = 0
        self.name = name
        self.age = age

    def add(self, num1):
        self.result += num1
        return self.result

    def sub(self, num1):
        self.result -= num1
        return self.result

    def mul(self, num1):
        self.result *= num1
        return self.result
    
    def div(self, num1):
        if num1 == 0:
            print("Error: 0으로 나눌 수 없습니다.")
            return self.result
        self.result /= num1
        return self.result

    def reset(self):
        self.result = 0
        return self.result

cal1 = Calculator("이민용", 25)
cal2 = Calculator("이동현", 20)
print(cal1) #self값이 출력, 인스턴스가 저장된 메모리
print(cal2)
print(cal1.name)
print(cal1.age)

print(cal1.result)

cal1.add(3)
cal1.mul(5)
cal1.sub(6)
cal1.div(7)
print(cal1.result)

cal1.reset()
print(cal1.result)
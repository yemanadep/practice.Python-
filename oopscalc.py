class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    @staticmethod
    def greet():
        print("Hello welocome bro!!")
a = Calculator(10)
a.greet()
a.square()

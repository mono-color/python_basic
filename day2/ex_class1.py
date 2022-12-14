class Rectangle:
    count = 0  # 클래스 변수

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        print('인스턴스메서드')
        return area

    @staticmethod
    def isSquare(rectWidth, rectHeight):
        print('정적메서드')

    @classmethod
    def printCount(cls):
        print('클래스메서드')
        cls.count = cls.count + 1
        return cls.count

    def __add__(self, other):
        obj = Rectangle(self.width * other.width, self.height * other.height)
        return obj


# 인스턴스화
my_r = Rectangle(10, 10)
my_r2 = Rectangle(10, 5)

my_r3 = my_r + my_r2
print(my_r3.width, my_r3.height)
# 인스턴스 메서드는 인스턴스가 있어야 실행 가능
print(my_r.calcArea())
# 클래스 메서드 클래스 자체로 실행 가능
print(Rectangle.printCount())
# 정적메서드 (클래스 변수에 접근 불가)
print(Rectangle.isSquare(5, 5))

# class calc:
#     def clac(self):
#         print("can calculate")
# class sum(calc):
#     def calc(self,a,b):
#         print("Sum is: ", a+b)
# b1=sum()
# b1.calc(5,3)

class shape:
    def calc(self):
        print("Can calculate")


class Sum(shape):
    def calc(self, a, b):
        print("Sum is:", a + b)


class triangle(shape):
    def calc(self, base, height):
        area = 0.5 * base * height
        print("Triangle area:", area)


class rectangle(shape):
    def calc(self, length, width):
        area = length * width
        print("Rectangle area:", area)


class circle(shape):
    def calc(self, r):
        area = 3.1416 * r * r
        print("Circle area:", area)


b1 = Sum()
t1 = triangle()
r1 = rectangle()
c1 = circle()

b1.calc(5, 10)
t1.calc(5, 10)
r1.calc(5, 10)
c1.calc(7)
import

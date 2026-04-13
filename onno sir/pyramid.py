# n=5
# for i in range(1,n+1):
#     print("*"*1)
#
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"Name : {self.name}, Age: {self.age}")
# p1 = student("Rahim", 20)
# p2 = student("Manik", 19)
# p1.show()
# p2.show()
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         self.area = length * width

#     def show(self):
#         print(f"Length: {self.length}, Width: {self.width}, Area: {self.area}")


# r1 = Rectangle(10, 5)
# r1.show()
#
#arms KI JANI,,
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("Area:", 3.1416 * self.radius * self.radius)


# c1 = Circle(5)
# c1.area()

class Armstrong:
    def __init__(self, num):
        self.num = num

    def check(self):
        power = len(str(self.num))
        temp = self.num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp //= 10

        if total == self.num:
            print(f"{self.num} is an Armstrong number")
        else:
            print(f"{self.num} is NOT an Armstrong number")


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

obj1 = Armstrong(n1)
obj2 = Armstrong(n2)

obj1.check()
obj2.check()
    
        

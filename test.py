# items=["milk", "banana","rice","dates","lentils"]
# find=str(input("Enter what is you cheking: "))

# if find in items:
#     print(find,"found")
# else:
#     print(find,"Not found")
#-----------------------------------------------------------
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
op=input("What you want to do for those two: ")
if op == "+":
    print("Yoour ans:", x+y)
elif op == "-":
    print("Your ans:", x-y)
elif op == "*":
    print("Your ans:", x*y)
elif op == "/":
    print("Your ans", x/y)
else:
    print("Invalid operator you have inputed")

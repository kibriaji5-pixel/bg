#Dictionary
student={
    "name":"Zim",
    "age":"18",
    "institute":"RPI"
}
print(student)
print(student["name"])
print(student.get("age"))
student["marks"]=87
print(student)
student["age"]=20
# print(student)
# student.clear()
# print(student)
# student.pop("name")
# print(student)
# del student["marks"]
# print(student)
print(student.keys())
print(student.values())
print(student.items)
print("marks" in student)


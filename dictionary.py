students=["bob",25,"tina",15,"jon",5]
students={"bob":25,"tina":15,"jon":5}
print(students["bob"])
students["bob"]=14
print(students)
del students["bob"]
print(students)
students.clear()
print(students)
students={"bob":25,"tina":15,"jon":5}
print(len(students))
print(students.keys())
print(students.values())
students2={"bobs":15,"tinas":35,"jons":25}
students.update(students2)
print(students)



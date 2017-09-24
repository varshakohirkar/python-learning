class Person:
	degree = "PhD"
	def __init__(self,n,a,d="BTech"):
		self.name = n
                self.age = a
		self.degree = d

	def displayInstance(self):
		print(self.name)
        	print(self.age)
        	print(self.degree)

person1=Person("varsha",24,"B.Tech")
person1.displayInstance()

"""
exit()
print("person 1")
Peson1 = Person("Varsha",24)
pint(Person1.name)
rint(Person1.age)

setattr(Person1,'sex',"female")
print(hasattr(Person1,"sex"))

print(Person1.degree)

print("-------------------------")
print("person 2")

Person2 = Person("Satish",27)
print(Person2.name)
print(Person2.age)
print(hasattr(Person1,"name"))
print(Person2.degree)
print("-------------------------")
print("person 3")
Person3 = Person("Varsha 2",24,"MS")
print(Person3.name)
print(Person3.age)
print(Person3.degree)"""

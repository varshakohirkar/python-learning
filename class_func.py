class Students:
	def __init__(self,name,age):
                self.name=name
                self.age=age

	def displayStudents(self):
		return("Student name is "+ self.name+" and age is "+str(self.age))





stu=Students("varsha",15)
print(stu.displayStudents())

          


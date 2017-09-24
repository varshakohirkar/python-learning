class Parent:
      counter=10
      age=24
      def __init__(self,counter,age):
                 self.counter=counter
                 self.age=age
      def parentFunc(self,counter):
                if counter >= 10:
                     print("enough students")
                else:
                     print("continue filling students")
      def setAge(self,age):
                if age >= 24:
                     print("not elligible")
                else:
                     print("elligible")

class child(Parent):
      def __init__(self):
                  print("Class initialized")
stu=Parent(12,25)
Student=child()
Student.parentFunc(9)
stu.setAge(25)
Student.setAge(21)

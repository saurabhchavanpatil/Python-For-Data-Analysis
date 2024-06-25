#MUlTIPLE INHERITAN
#  the one or more parent class can be
# accesible for child class,the accesible methode is nothing but ineritance
# Given Ex the Student And Marks is Parent class of Result class,Result clas
# is a child class of Student and Marks.
class Student:
     def __init__(self,n,r,a):
         self.name=n 
         self.roll=r
         self.address=a 

class Marks:
    m=55

class Result(Student,Marks):
    def result(self):
        if self.m>45:
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")
        
re=Result("Abc",555,"Pune")
re.result()

 


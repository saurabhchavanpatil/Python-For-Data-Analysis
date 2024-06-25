# Inheritance (Singal)
# the example is shows the how to inherite the methode in one class can access 
# in other class.

class A:
  a=10 
 
class B(A):
   b=5
   def su(self):
      return  self.b * self.a
   
myobj=B()
print(myobj.su())
   
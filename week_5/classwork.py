class  Employee:

  def __init__(self,name,age,role,salary):
   self.name = name
   self.age =age
   self.role =role
   self.salary =salary
    
  def information(self):
    return f"the enployee name is {self.name} , his age {self.age} , his role is {self.role} and his salary is {self.salary}."
  
joe = Employee(name="Tavershima", age=30, role="backend-dav", salary=40000)
print(joe.information())
  
class person:
    def __init__(self):
      self.name = "joe"
      
      
class employee(person):
    def __init__(self):
      super().__init__()
      
joe = employee()
print(joe.name)
  
class person:
  def __init__(self,name,age, gender):
   self.name = name
   self.age = age
   self.genger = gender
    
class Employee():
  def __init__(self, name, age, gender):
    super().__init__(name, age, gender)
    
  joe = Employee(name="joe saders", age=22, gender="male")
  print(joe.age)
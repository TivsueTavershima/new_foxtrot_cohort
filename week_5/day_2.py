



# OBJECT ORIENTED PROGRAMING(OOP):is a kind of programing when create a blue print called class and those class create object.
# FUNCTIONAL PROGRAMING:
# PROCEDURE PROGRAMING:

# MEASURE STRUCTURE: 
# ATTRIBUTE: attribute are qualities,characteristics.
# METHODS: is the action of clss that perform a specific task.for example,speaking or moving.

# TYPES OF ATTRIBUTE:
# 1. CLASS ATRRIBUTE - is an attribute that is common to all attribute.
# 2. INSTANCE ATTRIBUTE -is an attribute that is unique from each other.


class person:      #Blue print
   pass



Miracle = person()    # Object also called instance
Clinton = person()    # Object - instance
tivsue = person()     # object - instance


# The structure of the class
class footballer:
  
  #--Methods here ----
  game = "football"
  ball = "sphere"
  
  #--instance attribute --
  def __init__(self,name, age, role):  # constructor
    self.name = name
    self.age = age
    self.role = role
  

  #-----Method-----
  def information(self):
    return f"{self.name} plays {footballer.game}. the ball is {footballer.ball}"
  
  
zinedine_zidane = footballer("Zinedine Zidane", 34, "Attacking Midfielder")
christiano_ronaldo = footballer(name="Ronaldo", age=39, role="stricker")
  
print(zinedine_zidane.information())
print(zinedine_zidane.information())







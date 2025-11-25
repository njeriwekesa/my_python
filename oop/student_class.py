class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # def display_student_information(self):
  #   info = f"Name:{self.name} Age:{self.age}"
  #   return info
  
  def __str__(self):
    return f"Name: {self.name} Age: {self.age}"
  
student1 = Student("Njeri", 25)
print(student1)
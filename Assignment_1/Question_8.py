# Assignment 1
# January 16, 2004

# Question 8
# (a)
class Resturant:
  def __init__(self,resturant_name,cuisine_type):
    self.resturant_name = resturant_name
    self.cuisine_type = cuisine_type
  def describe_resturant(self):
    print(f'Resutrant Name: - {self.resturant_name}\nCuisine Type - {self.cuisine_type}')
  def open_resturant(self):
    print("The resturant is open!")

res = Resturant("The Street Cafe","Indian")
print(res.resturant_name)
print(res.cuisine_type)
res.describe_resturant()
res.open_resturant()

# (b)
class User:
  def __init__(self,first_name, last_name,email,reg_no,deptt,sub_group):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.reg_no = reg_no
    self.deptt = deptt
    self.sub_group = sub_group
  def describe_User(self):
    print(f"Name: {self.first_name +' '+ self.last_name}\nReg. No.: {self.reg_no}\nDeptt.: {self.deptt}\nSub-Group: {self.sub_group}\nEmail: {self.email}")
  def greet_User(self):
    print(f"Hi {self.first_name + ' ' + self.last_name}, Welcome to the TheStreetCafe!!😊🧡")
u = User("Ratn","Govindam","rg.ratn@gmail.com",102397020,"CSE","CS-10")
u.describe_User()
u.greet_User()

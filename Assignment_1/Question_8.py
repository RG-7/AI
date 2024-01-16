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

class Recipe:
    def __init__(self,Name,Ingredients,CookTime,Instructions):
        self.Name = Name
        self.Ingredients = Ingredients
        self.CookTime = CookTime
        self.Instructions = Instructions
       
    def display_recipe(self):
      print('Displaying recipe📜 ...')
      print(f"Name🍽️:{self.Name}")
      print(f"Ingredients🛒:{self.Ingredients}")
      print(f"Cooking Time⏳:{self.CookTime}")
      print(f"Instructions📖:{self.Instructions}")
      print("_"*20)

def create_recipe():  
        name_recipe=input("🔹Eneter recipe name: ")
        ingredients=input("🔹Eneter ingredients (comma-separated): ")
        cook_time=input("🔹Eneter cooking time: ")
        instructions=input("🔹Eneter cooking instructions: ")
        return Recipe(name_recipe,ingredients,cook_time,instructions) 
print("🎉🎉Welcome to the Recipe Collection🎉🎉\n")
recipe=create_recipe()
 
recipe.display_recipe()

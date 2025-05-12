#Tuples
#------
my_tuple = (1,2,3)

fruits =('apple','banana','cherry')
print(fruits[0])
print(fruits[-1])

coordinates =(10,20,30)

x, y, z = coordinates
print(x)
print(y)
print(z)

print(len(fruits))
print(fruits+('orange',))


#Sets
#-----

my_set = {1,2,3}

ingredients = {"flour","sugar","butter"}
ingredients.add("eggs")
ingredients.remove("sugar")
print(ingredients)

#Set Operations (Union, Intersection, Differences)
#-------------------------------------------------

set_a = {"flour","sugar","butter"}
set_b = {"sugar","eggs"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)


#Ingredient Checker (Project)
#----------------------------

#Define the recipe ingredients

recipe_ingredients = {"flour","sugar","butter","eggs","milk"}
user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

#Compare ingredients

missing_ingredients = recipe_ingredients-user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

print("\n--- Ingredient Check Results---")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed.")

if extra_ingredients:
    print(f"You are extra the following ingredients: {', '.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")
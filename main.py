# first task 

from pprint import pprint

with open('recipes.txt', 'rt') as file:
  cook_book = {}
  for el in file:
    dish_name = el.strip()
    indigrients_count = int(file.readline())
    composition = []
    for i in range(indigrients_count):
      emp = file.readline()
      ingredient_name, quantity, measure = emp.strip().split(' | ')
      composition_dish = {
        'ingredient_name':ingredient_name,
        'quantity': quantity,
        'measure': measure
      }
      composition.append(composition_dish)
    file.readline()
    cook_book [dish_name] = composition
  pprint(cook_book, sort_dicts=False)

  


    
  
    
  

  
    
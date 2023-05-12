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


# second task

def get_shop_list_by_dishes(dishes, person_count):
  indigrients_count = {}
  indigrient = {}

  for el in dishes:
    if el in cook_book.keys():
      for li in cook_book[el]:
        indigrient = {('measure': li['measure']),
                      indigrient['quantity'] = int(li['quantity']) * person_count
        print(indigrient)
        if li['ingredient_name'] in indigrients_count.keys():
          indigrient['quantity'] = indigrient['quantity'] + (int(li['quantity']) * person_count)
        else:
          indigrients_count[li['ingredient_name']] = indigrient

        print(indigrients_count)

        dishes = ['Омлет', 'Фахитос']
        get_shop_list_by_dishes(dishes, 10)
  


    
  
    
  

  
    
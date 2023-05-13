# first task

from pprint import pprint

with open('recipes.txt', 'rt', encoding = 'utf-8') as file:
    cook_book = {}
    for el in file:
        dish_name = el.strip()
        indigrients_count = int(file.readline())
        composition = []
        for i in range(indigrients_count):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            composition_dish = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            composition.append(composition_dish)
        file.readline()
        cook_book[dish_name] = composition
    pprint(cook_book, sort_dicts=False)



# second task

def get_shop_list_by_dishes(dishes, person_count):
    indigrients_count = {}
    indigrient = {}

    for el in dishes:
        if el in cook_book.keys():
            for li in cook_book[el]:
                indigrient = {'measure': li['measure']}
                indigrient['quantity'] = int(li['quantity']) * person_count
                if li['ingredient_name'] in indigrients_count.keys():
                    indigrient['quantity'] = indigrient['quantity'] + (int(li['quantity']) * person_count)
                else:
                    indigrients_count[li['ingredient_name']] = indigrient

    print(indigrients_count)


dishes = ['Омлет', 'Фахитос']
get_shop_list_by_dishes(dishes, 5)

# third task

with open('1.txt',encoding='utf-8') as file_1, open('2.txt',encoding='utf-8') as file_2, open('3.txt',encoding='utf-8') as file_3:
    dict_file = {}
    dict_file['1.txt'] = len(file_1.readlines())
    dict_file['2.txt'] = len(file_2.readlines())
    dict_file['3.txt'] = len(file_3.readlines())

    dict_file = sorted(dict_file.items(), key=lambda x: x[1])
    dict_sort = dict(dict_file)

with open('4.txt', 'w', encoding='utf-8') as file_4:
    for key, value in dict_sort.items():
        with open(key, encoding='utf-8') as file:
            f = file.readlines()
            res = ''.join(f)
        file_4.write(f'{key}\n{value}\n{res}\n')

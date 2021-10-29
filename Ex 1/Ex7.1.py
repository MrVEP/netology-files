from pprint import pprint


def cookbook_prep(file: str):
    cook_book = {}
    with open(file, encoding='UTF-8') as file:
        for line in file:
            dish = line.strip()
            ingredients = []
            for ingredient in range(int(file.readline())):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredients.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                )
            cook_book[dish] = ingredients
            file.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book: dict, dishes: list, person_count: int):
    groceries_list = {}

    for i in dishes:
        for j in cook_book.get(i):
            if j.get('ingredient_name') in groceries_list:
                if groceries_list[j.get('ingredient_name')]['measure'] == j.get('measure'):
                    groceries_list[j.get('ingredient_name')]['quantity'] += j.get('quantity')*person_count
                else:
                    temp = groceries_list[j.get('ingredient_name')]['measure']
                    convert = float(input(f"\nУкажите сколько {j.get('measure')} в {temp}: "))
                    groceries_list[j.get('ingredient_name')]['quantity'] += j.get('quantity') * person_count / convert
            else:
                groceries_list[j.get('ingredient_name')] = dict(measure=j.get('measure'),
                                                                quantity=j.get('quantity') * person_count)
    return groceries_list


def main():
    cookbook = cookbook_prep('recipes.txt')
    groceries = get_shop_list_by_dishes(cookbook, ['Запеченный картофель', 'Омлет'], 2)
    pprint(groceries)


main()

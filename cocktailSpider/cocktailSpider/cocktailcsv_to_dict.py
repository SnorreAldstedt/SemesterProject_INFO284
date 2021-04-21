import csv
import os

# Function makes the csv file a list of dicts with a specific format
# Could be used with other csv if it hhas the same format as cocktail_recipes.csv
# If csv have another format, csv_dict function have to be customized for that csv file
# ing_amount has index 0, ingredients: index 1, preparation: index 2, title: index 3 and url: index 4


def csv_dict(csv_file):
    list_dict = []
    with open(csv_file) as c:
        csv_reader = csv.DictReader(c)
        for r in csv_reader:
            keys = list(r.keys())
            prep = r[keys[2]].split(',')
            ing = r[keys[1]].split(',')
            ing_amount = r[keys[0]].split(',')
            ingredients = {}
            for n in range(len(ing)):
                ingredients[ing[n]] = ing_amount[n]
            list_dict.append(
                {'drink': r[keys[3]], 'ingredients': ingredients, 'preparation': prep, 'url': r[keys[4]]}
            )
    return list_dict


cocktail_listdict = csv_dict('cocktail_recipes.csv')
print(cocktail_listdict)

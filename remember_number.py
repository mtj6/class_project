import json

filename = 'fav_numbers.json'

try:
    with open(filename) as f_obj:
        fav_numbers = json.load(f_obj)
except FileNotFoundError:
    fav_numbers = input("What's your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(fav_numbers, f_obj)
        print("We'll remember your favorite number next time!")
else:
    print("I remember your favorite number! It's " + fav_numbers + ".")
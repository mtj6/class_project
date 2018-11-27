import json

filename = 'fav_numbers.json'

with open(filename) as f_obj:
    favorite = json.load(f_obj)
    print("I remember your favorite number! It's " + favorite + ".")
    
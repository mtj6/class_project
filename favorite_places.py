favorite_places = {
    'Jessica' : ['Istanbul', 'Budapest'],
    'Sam' : ['Chicago', 'Memphis'],
    'Sean' : ['Boulder', 'Portland', 'Salt Lake City'],
    }
for name, places in favorite_places.items():
    print(name)
    for place in places:
        print('\t' + place.title())
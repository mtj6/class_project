def city_country(city, country):
    """Return a city and its country."""
    full_name = city + ', ' + country
    return full_name.title()

print(city_country('berlin', 'germany'))
print(city_country('london', 'england'))
print(city_country('paris', 'france'))
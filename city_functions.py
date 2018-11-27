def city_country(city, country, population=''):
    """Generate a fomated name of a city."""
    if population:
        city_name = city.title() + ', ' + country.title() + ' - population ' + population
    else:
        city_name = city.title() + ', ' + country.title()
    return city_name
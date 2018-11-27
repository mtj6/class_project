def describe_city(city, country='UK'):
    """Name some cities."""
    print(city.title() + ' is in the ' + country.upper() + '.')
    
describe_city('london')
describe_city('oxford')
describe_city('new york city', country='US')
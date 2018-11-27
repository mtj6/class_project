cities = {
    'anchorage' : {
        'state' : 'alaska',
        'population' : '300000',
        'fact' : 'This city holds almost half the population of Alaska.',
        },
    'juneau' : {
        'state' : 'alaska',
        'population' : '30000',
        'fact' : 'This city was founded in 1881 by Joe Juneau.',
        },
    'spokane' : {
        'state' : 'washington',
        'population' : '250000',
        'fact' : 'Keyboard Cat lived in Spokane.'
        },
        
    }
for city, city_info in cities.items():
    print(city.title())
    state = city_info['state']
    population = city_info['population']
    fact = city_info['fact']
    
    print('\tState: ' + state.title())
    print('\tPopulation: ' + population)
    print('\tFact: ' + fact)

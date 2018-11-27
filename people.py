people = {
    'emily' : {
        'age' : '24', 
        'first name' : 'emily', 
        'last name' : 'leist', 
        'city' : 'Pasco',
        },
    'elizabeth' : {
        'age' : '25',
        'first name' : 'elizabeth',
        'last name' : 'hassebrock',
        'city' : 'seattle',
        },
    'elisa' : {
        'age' : '25',
        'first name' : 'elisa',
        'last name' : 'wilson',
        'city' : 'boulder',
        },
    }
for person, person_info in people.items():
    print('\nFirst Name: ' + person_info['first name'].title())
    print('Last Name: ' + person_info['last name'].title())
    print('Age: ' + person_info['age'])
    print('City: ' + person_info['city'].title())
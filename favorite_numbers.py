favorite_numbers = {
    'jamie' : ['4', '9'], 
    'sam' : ['5', '71'], 
    'jennifer' : ['28', '0', '1'], 
    'heather' : ['2', '8'], 
    'tom' : '3',
    }
for name, numbers in favorite_numbers.items():
    print(name.title())
    for number in numbers:
        print('\t' + number)
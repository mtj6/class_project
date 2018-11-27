rivers = {
    'danube' : {
        'country' : 'austria', 
        'length' : '1777 miles',
        },
    'seine' : {
        'country' : 'france',
        'length' : '482 miles',
        },
    'thames' : {
        'country' : 'england',
        'length' : '215 miles',
        },
    
    }
    
    
    
for river, river_info in rivers.items():
    country = river_info['country']
    length = river_info['length']
    print('The ' + river.title() + ' runs through ' + country.title() + ' and is ' + length + ' long.')

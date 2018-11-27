def build_car(make, model, **car_info):
    """Build a car."""
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car
    
car = build_car('subaru', 'outback', color='white', year='2008')
print(car)
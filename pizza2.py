pizzas = ["moose's tooth", "bear's tooth", "island pub"]
for pizza in pizzas:
    print(pizza)
    
for pizza in pizzas:
    print('I love ' + pizza.title() + ' pizza.')
    
print('I just love pizza!')

friend_pizza = pizzas[:]
pizzas.append('iron goat')
friend_pizza.append('bulwinkles')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)
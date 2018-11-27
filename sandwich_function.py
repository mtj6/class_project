def sandwich_toppings(*toppings):
    """Summarize the sandwich someone orders."""
    print('\nMaking a sandwich with the following toppings: ')
    for topping in toppings:
        print('- ' + topping)
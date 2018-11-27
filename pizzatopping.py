prompt = "\nWhat would you like on your pizza? "
prompt += "\nEnter 'quit' when you're done adding toppings. "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print("I'm adding " + topping + " to your pizza.")
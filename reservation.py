number = input('How many people are in your dinner group? ')
number = int(number)
if number > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
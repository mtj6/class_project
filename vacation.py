vacation = []
polling_active = True
while polling_active:
    response = input('\nIf you could visit one place in the world, where would you go? ')
    vacation.append(response)
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False
print('\nThe responses to our survey about dream vacations are: ')
for response in vacation:
    print(response)
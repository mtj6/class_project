sandwiches = ['blt', 'turkey club', 'breakfast']
finished = []

while sandwiches:
    current_sandwich = sandwiches.pop()
    print('I made your ' + current_sandwich + ' sandwich.')
    finished.append(current_sandwich)
print('\nThe following sandwiches are complete:')
for sandwich in finished:
    print(sandwich)
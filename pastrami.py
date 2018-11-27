sandwiches = ['pastrami', 'blt', 'turkey club', 'pastrami', 'breakfast', 'pastrami']
finished = []
print('The Deli has run out of pastrami.')
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
while sandwiches:
    current_sandwich = sandwiches.pop()
    print('I made your ' + current_sandwich + ' sandwich.')
    finished.append(current_sandwich)
print('\nThe following sandwiches are complete:')
for sandwich in finished:
    print(sandwich)
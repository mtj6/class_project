current_users = ['magnolia', 'maggiet', 'mtj6', 'maggie.htj' 'maggiehtj']
new_users = ['magnolia4556', 'mags', 'maggiehtj', 'maggiet', 'maggietj']
for name in new_users:
    if name in current_users:
        print('Username taken. Please enter a new username.')
    else:
        print('Username available.')
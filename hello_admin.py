names = ['heather', 'rebecca', 'tom', 'admin', 'george']
for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + name.title() + ', welcome back.')
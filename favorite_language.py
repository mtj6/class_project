favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

list = ['jen', 'samantha', 'sarah', 'jeremy', 'heather', 'frank', 'phil']

for name in list:
    if name in favorite_language.keys():
        print('Thank you for taking the survey, ' + name.title() + '.')
    else:
        print('Please take the survey, ' + name.title() + '.')
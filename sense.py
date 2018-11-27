filename = 'senseandsensibility.txt'

with open(filename) as f_obj:
        contents = f_obj.read()
        words = contents.lower()
        numwords = words.count('the')
        print(numwords)
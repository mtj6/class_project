from collections import OrderedDict

glossary = OrderedDict()

glossary['index'] = 'position of an item in a list'
glossary['list'] = 'a collection of items in a particuar order'
glossary['loop'] = 'a way to perform an action on every item in a list'
glossary['indentation errors'] = 'mistakes in levels of indentation'
glossary['dictionary'] = 'a collection of key-value pairs'

for key, value in sorted(glossary.items()):
    print(key.title() + ': ' + value + ".")
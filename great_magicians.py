def make_great(magicians, great_magicians):
    while magicians:
        current_magician = ('The Great ' + magicians.pop())
        great_magicians.append(current_magician)

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())        
    
magicians = ['houdini', 'merlin', 'harry potter']
great_magicians = []
make_great(magicians[:], great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)
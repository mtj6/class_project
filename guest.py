filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    prompt = ("\nPlease enter your name.")
    prompt += ("\nEnter q to quit.")
    
    while True:
        guest = input(prompt)
    
        if guest == 'q':
            break
        else:
            print("Hello and welcome, " + (guest.title()) + ".")
            file_object.write((guest.title()) + " visited.\n")
filename = "programming_poll.txt"

with open(filename, 'w') as file_object:
    prompt = "Tell me why you like programming:"
    prompt += "\nEnter q to quit. "

    while True:
        response = input(prompt)
    
        if response == 'q':
            break
        else:
            file_object.write((response) + "\n")
            print('')
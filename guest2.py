prompt = ("\nPlease enter your name.")
prompt += ("\nEnter q to quit.")
    
while True:
    guest = input(prompt)
    
    if guest == 'q':
        break
    else:
        print(guest.title())
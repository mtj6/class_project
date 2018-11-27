prompt = "\nEnter your age and I will tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    age = input(prompt)
    
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
        
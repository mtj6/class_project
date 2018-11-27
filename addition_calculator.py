print("Give me two numbers and I'll add them together.")
print("Enter q to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter your numbers in digit form.")
    else:
        print(answer)
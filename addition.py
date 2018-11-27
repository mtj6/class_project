print("Give me two numbers and I'll add them together.")

first_number = input("First number: ")
second_number = input("Second number: ")
    
try:
    answer = int(first_number) + int(second_number)
    print(answer)
except ValueError:
    print("Please enter your numbers in digit form.")

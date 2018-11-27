filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as file_object:
            for line in file_object:
                print(line.rstrip())
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)

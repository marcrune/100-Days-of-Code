# Opening a txt file, reading it and closing it manually so it doesn't consume too much of the computer's resources
file = open("E:/Downloads/Programação/Python/100 Days of Code/Day 24/my_file.txt")
contents = file.read()
print(contents)
file.close()

# Opening a file using "with... as..." so it closes the file automatically when I stop using it (opens file using the "read only" mode by default)
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Changing the mode parameter to write so it's possible to write information on the file (will delete all existing text)
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Changing the mode parameter to append so it's possible to write information on the file without deleting all existing text
with open("my_file.txt", mode="a") as file:
    file.write("New text.")
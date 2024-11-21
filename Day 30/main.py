# "Try catch except finally" pattern

try:
    # Tries to execute following lines of code
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    # If FileNotFoundError occurs it creates the file using the "write" mode
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    # If KeyError occurs, it prints the non-existent key
    print(f"The key {error_message} does not exist.")
else:
    # If the "try" succeeds, it reads the file and prints its content
    content = file.read()
    print(content)
finally:
    # Will always close the file no matter what happens before
    file.close()
    print("File was closed.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    # Even though there are no problems in the code, it raises a developer created error because the height is unrealistic
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
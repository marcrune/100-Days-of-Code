#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Terminal must be in the "day 24" folder for this to run
with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_as_list = letter.readlines()

with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    names_as_list = names.readlines()

customized_letter = []

# Replacing the "[name]" with every name on the invite list and then appending it to the customized_letter list
for line in letter_as_list:
    for name in names_as_list:
        if "[name]" in line:
            x = line.replace("[name]", name.strip())
            customized_letter.append([x])

# Adding every other line to each invitation
for lst in customized_letter:
    for line in letter_as_list[1:]:
        lst.append(line)

# Using the enumerate function to create tuples associating numbers with the names and using the numbers as the index for the customized_letter list
for i, name in enumerate(names_as_list):
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w+") as invitation:
        invitation.write("".join(customized_letter[i]))
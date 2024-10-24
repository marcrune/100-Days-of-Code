# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo", "C": "Charlie"}


# TODO 2. Create a list of phonetic code words from a word that the user inputs.

import pandas as pd

# Reading the CSV
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary from the dataframe
df_dict = {index:row for (index, row) in df.iterrows()}
# df_dict = {row.letter:row.code for (index, row) in df.iterrows()} -- solution to obtain the clean dictionary with a single line of code

# Cleaning the df_dict and leaving only the letters and their respective words
code_words = {letter:word for (letter, word) in df_dict.values()}

# Asking the user for an input to be translated
alpha = False

while not alpha:
    user_input = input("Say a word to be translated to the NATO alphabet code words: ")
    try:
        # Trying to create a list with the corresponding words for each letter in the user input if its alphabetic
        answer = [code_words[letter] for letter in user_input.upper()]
    except KeyError:
        # If theres a KeyError, it prompts the user again until it types a valid entry (can also be done using recursion)
        print("Sorry, only letters in the alphabet please.")
    else:
        # When the input is valid, it prints the answer and stops the loop
        print(answer)
        alpha = True
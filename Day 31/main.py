import tkinter
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashy")
window.config(width=800, height=526, padx=50, pady=50, background=BACKGROUND_COLOR)

# -------------------------------------- DATA --------------------------------------
try:
    data = pd.read_csv("./data/words_to_learn.csv")
    print("Loaded words_to_learn.csv.")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    print("Loaded french_words.csv.")

data_dict = data.to_dict(orient="records")

# -------------------------------------- FUNCTIONS --------------------------------------
word = ""
# Random word function
def random_word():
    """Picks a random french word and puts it into the canvas."""
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(data_dict)["French"]
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, text=data.columns[0], fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")
    flip_timer = window.after(3000, turn_card)

# Right answer function
def right_answer():
    """Removes chosen word from the list if the user already knows it and picks a new french word."""
    for dict in data_dict:
        if dict["French"] == word:
            words_to_learn = data_dict
            words_to_learn.remove(dict)
            words_to_learn = pd.DataFrame(words_to_learn)
            words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    random_word()

# Get english translation function
def get_english_translation():
    """Returns the english translation of a french word."""
    for dict in data_dict:
        if dict["French"] == word:
            return dict["English"]

# Turn card function
def turn_card():
    """Turns the card showing the english word after 3 seconds."""
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text=data.columns[1], fill="white")
    canvas.itemconfig(card_word, text=get_english_translation(), fill="white")

# -------------------------------------- UI CONFIG --------------------------------------
# Canvas
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="./images/card_front.png")
back_image = tkinter.PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text=data.columns[0], font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
flip_timer = window.after(3000, func=turn_card)

# Buttons
right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

random_word()

window.mainloop()
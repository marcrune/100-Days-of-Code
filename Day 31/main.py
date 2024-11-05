import tkinter
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashy")
window.config(width=800, height=526, padx=50, pady=50, background=BACKGROUND_COLOR)

# -------------------------------------- DATA --------------------------------------
data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")

# -------------------------------------- UI CONFIG --------------------------------------
# Canvas
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
logo_img = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
card_title = canvas.create_text(400, 150, text=data.columns[0], font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=choice(data["French"]), font=("Ariel", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Random word function
def random_word():
    """Picks a random french word and puts it into the canvas."""
    word = choice(data["French"])
    canvas.itemconfig(card_word, text=word)

# Buttons
right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=random_word)
right_button.grid(column=1, row=1)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

window.mainloop()
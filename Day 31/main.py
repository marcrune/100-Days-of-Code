import tkinter

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashy")
window.config(width=800, height=526, padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
logo_img = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)


window.mainloop()
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# Different ways of changing label properties
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
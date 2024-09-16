import tkinter

# Window settings
window = tkinter.Tk()
window.title("Miles to Kilometers Calculator")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Labels
label_1 = tkinter.Label(text="is equal to")
label_1.grid(column=1, row=2)

label_2 = tkinter.Label(text="Miles")
label_2.grid(column=3, row=1)

label_3 = tkinter.Label(text="Km")
label_3.grid(column=3, row=2)

result = tkinter.Label(text="0")
result.grid(column=2, row=2)

# Entry
input = tkinter.Entry(width=7)
input.grid(column=2, row=1)

# Button
def miles_to_km():
    result["text"] = str(round(int(input.get()) * 1.609, 2))

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)


window.mainloop()
import tkinter
import tkinter.messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates the password and copies it to the clipboard."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Writes the website, e-mail/user and password to the data.txt file and clears all fields except e-mail/user afterwards."""
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        tkinter.messagebox.showwarning(title="Oops", message="Please don't leave any of the fields empty.")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: {user_entry.get()} "
                                            f"\nPassword: {password_entry.get()} \nIs it ok to save?")
        
        if is_ok:
            with open("./data.txt", mode="a") as file:
                file.write(f"{website_entry.get().title()} | {user_entry.get()} | {password_entry.get()}\n")
        
            clear_fields()


def clear_fields():
    """Clears website and password entry fields."""
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
# Window settings
window = tkinter.Tk()
window.config(padx=35, pady=35)
window.title("Password Manager")

# Creating canvas and the logo image
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

# Email/Username label
user_label = tkinter.Label(text="Email/Username:")
user_label.grid(column=0, row=2)

# Password label
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Website entry
website_entry = tkinter.Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Email/Username entry
user_entry = tkinter.Entry(width=50)
user_entry.insert(0, "marcoferrini@hotmail.com")
user_entry.grid(column=1, row=2, columnspan=2)

# Password entry
password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3)

# Generate password button
generate_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3, sticky="W")

# Add button
add_button = tkinter.Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
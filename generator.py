import tkinter as tk
from random import randint, choice, shuffle

password_length = 16
password = ""

# Generate valid password characters from ASCII codes
list_upper = []
list_lower = []
list_number = []
list_symbol = []

# Generate list of Uppercase characters
for i in range(65, 91):
    list_upper.append(chr(i))

# Generate list of Lowercase characters
for i in range(97, 123):
    list_lower.append(chr(i))

# Generate list of numbers
for i in range(48, 58):
    list_number.append(chr(i))

# Generate list of symbols
for i in range(33, 48):
    list_symbol.append(chr(i))
for i in range(58, 65):
    list_symbol.append(chr(i))
for i in range(91, 97):
    list_symbol.append(chr(i))
for i in range(123, 127):
    list_symbol.append(chr(i))


# ---------------------------------

def scale(val):
    global password_length
    password_length = int(val)
    do_it()


def do_it():
    global password
    password = ""
    remaining = password_length

    # Get current values
    password_upper = check_upper.get()
    password_lower = check_lower.get()
    password_number = check_number.get()
    password_symbol = check_symbol.get()
    password_number_qty = int(spinbox_number.get())
    password_symbol_qty = int(spinbox_symbol.get())

    # Restrict numbers and symbols to half the password length
    if password_number and password_number_qty > password_length / 2:
        password_number_qty = password_length // 2
        spinbox_number["to"] = password_number_qty
    if password_symbol and password_symbol_qty > password_length / 2:
        password_symbol_qty = password_length // 2
        spinbox_symbol["to"] = password_symbol_qty

    # Generate the password
    if password_symbol:
        for _ in range(0, password_symbol_qty):
            password += choice(list_symbol)
        remaining = password_length - len(password)
    if password_number:
        for _ in range(0, password_number_qty):
            password += choice(list_number)
        remaining = password_length - len(password)
    if password_lower and remaining > 0:
        if password_upper:
            qty_lower = randint(1, remaining)
        else:
            qty_lower = remaining
        for _ in range(1, qty_lower):
            password += choice(list_lower)
        remaining = password_length - len(password)
    if password_upper and remaining > 0:
        for _ in range(0, remaining):
            password = password + choice(list_upper)
    list_password = list(password)
    shuffle(list_password)
    password = "".join(list_password)
    label_password["text"] = password


# def generator_popup():

popup = tk.Tk()
popup.title("Password Generator")
popup.config(padx=30, pady=30)

length_pwd = tk.IntVar()
check_upper = tk.IntVar()
check_upper.set(1)  # Default to checked
check_lower = tk.IntVar()
check_lower.set(1)  # Default to checked
check_number = tk.IntVar()
check_symbol = tk.IntVar()

label_password = tk.Label(text="Password", width=20, height=3, fg="blue", font=("Sergoe UI", 12, "bold"), wraplength=200)
scale_length = tk.Scale(popup, label="Password Length", from_=6, to=48, length=140, orient=tk.HORIZONTAL, command=scale)
scale_length.set(password_length)
checkbox_upper = tk.Checkbutton(popup, text="Use A-Z", variable=check_upper, command=do_it)
checkbox_lower = tk.Checkbutton(popup, text="Use a-z", variable=check_lower, command=do_it)
checkbox_number = tk.Checkbutton(popup, text="Use 0-9", variable=check_number, command=do_it)
checkbox_symbol = tk.Checkbutton(popup, text="Use !@#$%^&*", variable=check_symbol, command=do_it)
spinbox_number = tk.Spinbox(popup, from_=1, to=9, width=3, command=do_it)
spinbox_symbol = tk.Spinbox(popup, from_=1, to=9, width=3, command=do_it)
label_number = tk.Label(popup, text="How many numbers")
label_symbol = tk.Label(popup, text="How many symbols")


# ---------------------------------

# Layout
label_password.grid(row=0, column=0, columnspan=3)
scale_length.grid(row=1, column=0, columnspan=3)
checkbox_upper.grid(row=2, column=1, sticky=tk.W)
checkbox_lower.grid(row=3, column=1, sticky=tk.W)
checkbox_number.grid(row=4, column=1, sticky=tk.W)
checkbox_symbol.grid(row=5, column=1, sticky=tk.W)
spinbox_number.grid(row=6, column=2)
spinbox_symbol.grid(row=7, column=2)
label_number.grid(row=6, column=0, columnspan=2)
label_symbol.grid(row=7, column=0, columnspan=2)

# ---------------------------------

popup.mainloop()

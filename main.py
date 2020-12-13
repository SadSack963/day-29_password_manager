import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

label_website = tk.Label(text="Website:")
label_email = tk.Label(text="Email / Username:")
label_password = tk.Label(text="Password:")

entry_website = tk.Entry(width=35)
entry_email = tk.Entry(width=35)
entry_password = tk.Entry(width=21)

button_generate = tk.Button(text="Generate Password")
button_add = tk.Button(text="Add", width=36)


# Grid layout
canvas.grid(row=0, column=1)
label_website.grid(row=1, column=0, sticky=tk.E)
label_email.grid(row=2, column=0, sticky=tk.E)
label_password.grid(row=3, column=0, sticky=tk.E)
entry_website.grid(row=1, column=1, columnspan=2, sticky=tk.EW)
entry_email.grid(row=2, column=1, columnspan=2, sticky=tk.EW)
entry_password.grid(row=3, column=1, sticky=tk.EW)
button_generate.grid(row=3, column=2, sticky=tk.EW)
button_add.grid(row=4, column=1, columnspan=2, sticky=tk.EW)


# ---------------------

window.mainloop()

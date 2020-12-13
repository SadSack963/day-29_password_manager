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

label_website = tk.Label(text="Website:", width=17)
label_email = tk.Label(text="Email / Username:", width=17)
label_password = tk.Label(text="Password:", width=17)

text_website = tk.Text(width=35, height=1)
text_email = tk.Text(width=35, height=1)
text_password = tk.Text(width=21, height=1)

button_generate = tk.Button(text="Generate Password")
button_add = tk.Button(text="Add", width=36)


# Grid layout
canvas.grid(row=0, column=1)
label_website.grid(row=1, column=0)
label_email.grid(row=2, column=0)
label_password.grid(row=3, column=0)
text_website.grid(row=1, column=1, columnspan=2)
text_email.grid(row=2, column=1, columnspan=2)
text_password.grid(row=3, column=1)
button_generate.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2)


# ---------------------

window.mainloop()

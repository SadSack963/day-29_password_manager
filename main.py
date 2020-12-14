import tkinter as tk  # import tkinter classes
# NOTE: messagebox is a separate module from tkinter which is not imported unless specified
from tkinter import messagebox




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    import generator
    password = generator.password
    print(password)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, generator.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Error", message="Please fill in all fields.")
    else:
        response = messagebox.askokcancel(title="Please confirm", message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n\nOK to save?")
        if response:
            # encoding="utf-16" allows extended unicode characters to be written to file
            with open("data.txt", mode="a", encoding="utf-16") as file:
                file.write(website + ", " + email + ", " + password + "\n")
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(window, width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

label_website = tk.Label(window, text="Website:")
label_email = tk.Label(window, text="Email / Username:")
label_password = tk.Label(window, text="Password:")

entry_website = tk.Entry(window, width=35)
entry_website.focus()
entry_email = tk.Entry(window, width=35)
entry_email.insert(0, "jwmp5051@gmail.com")  # Insert string just before the character indicated by index.
entry_password = tk.Entry(window, width=21)

button_generate = tk.Button(window, text="Generate Password", command=generate)
button_add = tk.Button(window, text="Add", width=36, command=save)


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

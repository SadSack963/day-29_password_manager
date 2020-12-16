import tkinter as tk  # import tkinter classes
from random import randint, choice, shuffle
# import string

TITLE_FONT = ("Sergoe UI", 16, "bold")
PWD_FONT = ("Sergoe UI", 12, "bold")
NORMAL_FONT = ("Sergoe UI", 10, "normal")
LARGE_FONT = ("Sergoe UI", 12, "normal")


# Lists of valid password characters
list_upper = []
list_lower = []
list_number = []
list_symbol = []


def get_list_of_chars():
    # https://www.journaldev.com/23788/python-string-module
    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.hexdigits)
    # print(string.octdigits)
    # print(string.whitespace)  # ' \t\n\r\x0b(VT)\x0c(FF)'
    # print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # print(string.printable)

    """Generate valid password characters from ASCII codes"""
    global list_upper, list_lower, list_number, list_symbol

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


class Popup():
    """Creates a new popup window containing the widgets allowing the user to create a random password"""
    global list_symbol, list_number, list_lower, list_upper

    def __init__(self, master):
        # Define variables
        self.password = ""
        self.password_length = 16
        self.password_upper = 1
        self.password_lower = 1
        self.password_number = 0
        self.password_symbol = 0
        self.password_number_qty = 4
        self.password_symbol_qty = 2
        self.qty_lower = 0
        self.list_password = []
        self.remaining = 16

        # UI Setup
        self.popup = tk.Toplevel(master)
        self.popup.title("Password Generator")
        self.popup.config(padx=30, pady=30)

        self.length_pwd = tk.IntVar()
        self.check_upper = tk.IntVar()
        self.check_upper.set(1)  # Default to checked
        self.check_lower = tk.IntVar()
        self.check_lower.set(1)  # Default to checked
        self.check_number = tk.IntVar()
        self.check_symbol = tk.IntVar()

        self.label_title = tk.Label(self.popup, text="Password Generator", pady=5, fg="dark green", font=TITLE_FONT)
        self.label_password = tk.Label(self.popup, text="Password", width=20, height=3, relief="sunken", bg="#cccccc",
                                       fg="blue", font=PWD_FONT, wraplength=200)
        self.scale_length = tk.Scale(self.popup, label="Password Length", from_=6, to=48, length=200, font=NORMAL_FONT,
                                     orient=tk.HORIZONTAL, command=self.scale)
        self.checkbox_upper = tk.Checkbutton(self.popup, text="Use A-Z", font=NORMAL_FONT, variable=self.check_upper,
                                             command=self.do_it)
        self.checkbox_lower = tk.Checkbutton(self.popup, text="Use a-z", font=NORMAL_FONT, variable=self.check_lower,
                                             command=self.do_it)
        self.checkbox_number = tk.Checkbutton(self.popup, text="Use 0-9", font=NORMAL_FONT, variable=self.check_number,
                                              command=self.do_it)
        self.checkbox_symbol = tk.Checkbutton(self.popup, text="Use !@#$%^&*", font=NORMAL_FONT,
                                              variable=self.check_symbol, command=self.do_it)
        self.spinbox_number = tk.Spinbox(self.popup, from_=1, to=9, width=3, font=LARGE_FONT, command=self.do_it)
        self.spinbox_symbol = tk.Spinbox(self.popup, from_=1, to=9, width=3, font=LARGE_FONT, command=self.do_it)
        self.label_number = tk.Label(self.popup, text="How many numbers", font=NORMAL_FONT, pady=5)
        self.label_symbol = tk.Label(self.popup, text="How many symbols", font=NORMAL_FONT, pady=5)
        self.button_close = tk.Button(self.popup, text="Close", font=NORMAL_FONT, command=self.close)

        self.scale_length.set(self.password_length)

        # ---------------------------------

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=3)
        self.label_password.grid(row=1, column=0, columnspan=3)
        self.scale_length.grid(row=2, column=0, columnspan=3)
        self.checkbox_upper.grid(row=3, column=1, sticky=tk.W)
        self.checkbox_lower.grid(row=4, column=1, sticky=tk.W)
        self.checkbox_number.grid(row=5, column=1, sticky=tk.W)
        self.checkbox_symbol.grid(row=6, column=1, sticky=tk.W)
        self.label_number.grid(row=7, column=0, columnspan=2)
        self.spinbox_number.grid(row=7, column=2)
        self.label_symbol.grid(row=8, column=0, columnspan=2)
        self.spinbox_symbol.grid(row=8, column=2)
        self.button_close.grid(row=9, column=0, columnspan=3)

        # ---------------------------------

        self.popup.mainloop()

    def scale(self, val):
        # This routine is required because tk.Scale() passes one string value to the called function
        self.password_length = int(val)
        self.do_it()

    def do_it(self):
        """Create the password every time a widget is altered"""
        self.password = ""  # Clear out any existing password
        self.remaining = self.password_length  # Number of characters in password yet to be filled

        # Get current values of checkboxes and spinboxes
        self.password_upper = self.check_upper.get()
        self.password_lower = self.check_lower.get()
        self.password_number = self.check_number.get()
        self.password_symbol = self.check_symbol.get()
        self.password_number_qty = int(self.spinbox_number.get())
        self.password_symbol_qty = int(self.spinbox_symbol.get())

        # Restrict numbers and symbols to half the password length
        if self.password_number:
            self.spinbox_number["to"] = self.password_length // 2
        if self.password_symbol:
            self.spinbox_symbol["to"] = self.password_length // 2

        # Generate the password
        if self.password_symbol:
            for _ in range(0, self.password_symbol_qty):
                self.password += choice(list_symbol)
            self.remaining = self.password_length - len(self.password)
        if self.password_number:
            for _ in range(0, self.password_number_qty):
                self.password += choice(list_number)
            self.remaining = self.password_length - len(self.password)
        if self.password_lower and self.remaining > 0:
            if self.password_upper:
                self.qty_lower = randint(1, self.remaining)
            else:
                self.qty_lower = self.remaining
            for _ in range(1, self.qty_lower):
                self.password += choice(list_lower)
            self.remaining = self.password_length - len(self.password)
        if self.password_upper and self.remaining > 0:
            for _ in range(0, self.remaining):
                self.password = self.password + choice(list_upper)
        self.list_password = list(self.password)
        shuffle(self.list_password)
        self.password = "".join(self.list_password)
        self.label_password["text"] = self.password

    def close(self):
        self.popup.quit()  # This allows the password to be accessed by main.py
        self.popup.destroy()  # Then destroy this script window

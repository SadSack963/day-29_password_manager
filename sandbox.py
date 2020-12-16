import tkinter as tk
import json

window = tk.Tk()

r = tk.Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = tk.Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = tk.Label(bg="blue", width=20, height=5)
b.grid(row=2, column=0, columnspan=2)


# JSON File Handling
# ==================

website = "Twitter"
email = "john@example.com"
password = "cvgyhui90-"

new_data = {website: {"email": email, "password": password}}

# encoding="utf-16" allows extended unicode characters to be written to file
# Save as CSV:
with open("data.txt", mode="a", encoding="utf-8") as file:
    file.write(website + ", " + email + ", " + password + "\n")

# Save as JSON:
# JSON files are written by dump, so mode is write instead of append
with open("data.json", mode="w", encoding="utf-8") as file:
    json.dump(new_data, fp=file, indent=4)

# Read JSON data:
with open("data.json", mode="r", encoding="utf-8") as file:
    data = json.load(fp=file)
    print(data)

# Update JSON file:
with open("data.json", mode="r", encoding="utf-8") as file:
    data = json.load(fp=file)
    data.update(new_data)
with open("data.json", mode="w", encoding="utf-8") as file:
    json.dump(data, fp=file, indent=4)


window.mainloop()

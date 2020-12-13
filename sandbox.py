import tkinter as tk

window = tk.Tk()

r = tk.Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = tk.Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = tk.Label(bg="blue", width=20, height=5)
b.grid(row=2, column=0, columnspan=2)

window.mainloop()

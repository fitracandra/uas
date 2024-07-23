import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

root = tk.Tk()
root.title("Simple GUI")

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()

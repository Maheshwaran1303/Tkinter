import tkinter as tk

# Function to append characters to the expression
def press(key):
    entry.insert(tk.END, key)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry widget for display
entry = tk.Entry(root, font=('Arial', 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

# Button text layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="C", width=22, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Start main loop
root.mainloop()

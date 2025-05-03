import tkinter as tk

# Function to update the display
def button_click(number):
    current = display_var.get()
    display_var.set(current + str(number))

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear():
    display_var.set("")

# Create the root window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Create a display variable to show the input/output
display_var = tk.StringVar()

# Display label (use grid instead of pack)
display = tk.Label(root, textvariable=display_var, height=2, font=("Arial", 24), relief="sunken", anchor="e")
display.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# Buttons for numbers and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Loop to create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=evaluate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=clear)
    else:
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()

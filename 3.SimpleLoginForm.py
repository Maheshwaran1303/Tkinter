import tkinter as tk

# Function to handle submit button click
def submit():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}")
    print(f"Password: {password}")
    result_label.config(text="Login Submitted!")

# Function to handle reset button click
def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, padx=10, pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# Label to show result
result_label = tk.Label(root, text="", fg="green")
result_label.grid(row=3, column=0, columnspan=2)

# Start the main loop
root.mainloop()

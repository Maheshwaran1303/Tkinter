import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Submit function
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email format!")
        return

    messagebox.showinfo("Success", "Registration Successful!")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("350x250")

# Optional: Set an icon (place your icon.ico in the same folder)
# Uncomment the next line after placing your icon
# root.iconbitmap("icon.ico")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Entry Fields
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

name_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Submit Button using pack()
submit_btn = tk.Button(root, text="Submit", command=submit_form)
# submit_btn.pack(pady=20)
submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()

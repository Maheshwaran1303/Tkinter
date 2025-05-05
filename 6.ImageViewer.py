import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.png")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=img_tk)
        canvas.image = img_tk
        
# Main Window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.iconbitmap("tkinter.png")

# Canvas for Image
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(padx=10, pady=10)

# Open Image Button
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)
root.mainloop()
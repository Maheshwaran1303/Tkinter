import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x200")

# Global variables
counter = 0
running = False

# Function to update the label every second
def update_time():
    global counter
    if running:
        minutes, seconds = divmod(counter, 60)
        hours, minutes = divmod(minutes, 60)
        time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        counter += 1
        root.after(1000, update_time)

# Start the stopwatch
def start():
    global running
    if not running:
        running = True
        update_time()

# Stop the stopwatch
def stop():
    global running
    running = False

# Reset the stopwatch
def reset():
    global counter, running
    running = False
    counter = 0
    time_label.config(text="00:00:00")

# Time display
time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 30))
time_label.pack(pady=20)

# Buttons
start_btn = tk.Button(root, text="Start", width=10, command=start)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", width=10, command=stop)
stop_btn.pack(pady=5)

reset_btn = tk.Button(root, text="Reset", width=10, command=reset)
reset_btn.pack(pady=5)

# Start the GUI event loop
root.mainloop()

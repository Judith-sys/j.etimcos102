import tkinter as tk
from tkinter import messagebox

# Function to handle the submit event
def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        messagebox.showinfo("Login", f"Welcome {username}!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Hide password text
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Create the main window (root)
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Function to display a welcome message
def welcomeMessage(username):
    window = tk.Toplevel(root)  # Create a new window
    window.title("Admin Box")
    window.geometry("500x200")
    
    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    
    label_2 = tk.Label(window, text="This is Python GUI with Tkinter")
    label_2.pack()

# Function to handle login submission
def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create label and entry fields for login
label_username = tk.Label(root, text="Username:")
label_username.pack()

username_entry = tk.Entry(root)
username_entry.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

password_entry = tk.Entry(root, show="*")  # Hide password input
password_entry.pack()

# Create the submit button
submit_button = tk.Button(root, text="Login", command=submit)
submit_button.pack()

# Run the Tkinter event loop
root.mainloop()

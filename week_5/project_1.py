import tkinter as tk
from tkinter import messagebox
import csv

# Function to load the employee data from the CSV file
def load_employee_data():
    employees = []
    with open('GIG-logistics.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

# Function to check if the user is an employee and return other department members
def check_employee(name, department):
    employees = load_employee_data()
    found_employee = False
    department_members = []

    # Iterate through the list to check for the employee and collect department members
    for employee in employees:
        if employee['Name'].lower() == name.lower() and employee['Department'].lower() == department.lower():
            found_employee = True
        if employee['Department'].lower() == department.lower():
            department_members.append(employee['Name'])

    if found_employee:
        return department_members
    else:
        return None

# Function to handle the submit button click
def submit():
    name = name_entry.get()
    department = department_entry.get()

    # Check if the employee exists
    department_members = check_employee(name, department)
    
    if department_members:
        # Display the welcome message and department members
        members_str = "\n".join(department_members)
        messagebox.showinfo("Welcome", f"Welcome {name}! You are a part of the {department} department.\nOther members of your department:\n{members_str}")
    else:
        # If the employee is not found, display an error message
        messagebox.showerror("Error", "Sorry, this employee does not exist.")

# Create the main window (root)
root = tk.Tk()
root.title("GIG Logistics Employee Verification")
root.geometry("400x200")

# Create the name input field and label
label_name = tk.Label(root, text="Enter your name:")
label_name.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Create the department input field and label
label_department = tk.Label(root, text="Enter your department:")
label_department.pack(pady=5)
department_entry = tk.Entry(root)
department_entry.pack(pady=5)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the main event loop
root.mainloop()

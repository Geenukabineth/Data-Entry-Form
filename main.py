import tkinter
from tkinter import ttk
from tkinter import messagebox


course_fees = {
    "Data Science": 15000,
    "Business": 12000,
    "Personal Development": 10000,
    "Computer Science": 20000
}

def calculate_balance():
    try:
        paid_amount = float(paid_amount_entry.get())
    except ValueError:
        paid_amount = 0.0


    course_selected = course_combobox.get()
    total_payment = course_fees.get(course_selected, 0)  

   
    if registered_check_var.get() == 0:
        total_payment += 1000

   
    balance = total_payment - paid_amount
    balance_amount_var.set(f"{balance:.2f}")  

def save_data():
 
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    registered = "Yes" if registered_check_var.get() else "No"
    
    
    paid_status = paid_combobox.get()
    paid_amount = paid_amount_entry.get()
    balance_amount = balance_amount_var.get()
    course_selected = course_combobox.get()

    with open("user_data.txt", "a") as file:
        file.write(f"First Name: {first_name}, Last Name: {last_name}, Title: {title}, Age: {age}, Nationality: {nationality}, "
                   f"Registered: {registered}, Paid: {paid_status}, Paid Amount: {paid_amount}, "
                   f"Balance: {balance_amount}, Course: {course_selected}\n")

    
    messagebox.showinfo("Data Saved", "Your data has been successfully saved!")
    
    clear_fields()

def clear_fields():
    """Clear all input fields."""
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    title_combobox.set('')
    age_spinbox.delete(0, tkinter.END)
    nationality_combobox.set('')
    registered_check_var.set(0)
    paid_combobox.set('')
    paid_amount_entry.delete(0, tkinter.END)
    balance_amount_var.set('')
    course_combobox.set('')

window = tkinter.Tk()
window.title("Data Entry Form")
window.config(bg="#f0f0f0")  

frame = tkinter.Frame(window, bg="#f0f0f0")
frame.pack()


user_info_frame = tkinter.LabelFrame(frame, text="User Information", bg="#f0f0f0")
user_info_frame.grid(row=0, column=0)


first_name_label = tkinter.Label(user_info_frame, text="First Name", bg="#f0f0f0")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name", bg="#f0f0f0")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)


title_label = tkinter.Label(user_info_frame, text="Title", bg="#f0f0f0")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)


age_label = tkinter.Label(user_info_frame, text="Age", bg="#f0f0f0")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=10, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="Nationality", bg="#f0f0f0")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Sri Lanka", "India", "Germany"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tkinter.LabelFrame(frame, text="Courses Information", bg="#f0f0f0")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)


registered_label = tkinter.Label(courses_frame, text="Registered Status", bg="#f0f0f0")
registered_label.grid(row=0, column=0)
registered_check_var = tkinter.IntVar()
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=registered_check_var, command=calculate_balance, bg="#f0f0f0")
registered_check.grid(row=1, column=0)

course_label = tkinter.Label(courses_frame, text="Course", bg="#f0f0f0")
course_combobox = ttk.Combobox(courses_frame, values=list(course_fees.keys()))
course_label.grid(row=2, column=0)
course_combobox.grid(row=3, column=0)
course_combobox.bind("<<ComboboxSelected>>", lambda event: calculate_balance())  

payment_frame = tkinter.LabelFrame(frame, text="Payment Information", bg="#f0f0f0")
payment_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)


paid_label = tkinter.Label(payment_frame, text="Payment", bg="#f0f0f0")
paid_combobox = ttk.Combobox(payment_frame, values=["full Paid", "Fully Not Paid"])
paid_label.grid(row=0, column=0)
paid_combobox.grid(row=1, column=0)


paid_amount_label = tkinter.Label(payment_frame, text="Paid Amount", bg="#f0f0f0")
paid_amount_entry = tkinter.Entry(payment_frame)
paid_amount_entry.grid(row=1, column=1)
paid_amount_label.grid(row=0, column=1)

# Balance Amount
balance_amount_label = tkinter.Label(payment_frame, text="Balance Amount", bg="#f0f0f0")
balance_amount_var = tkinter.StringVar()  # Using StringVar to auto-update balance
balance_amount_entry = tkinter.Entry(payment_frame, textvariable=balance_amount_var, state='readonly')
balance_amount_entry.grid(row=1, column=2)
balance_amount_label.grid(row=0, column=2)

# Update balance automatically when paid amount is entered
paid_amount_entry.bind("<KeyRelease>", lambda event: calculate_balance())

# Save and Clear Buttons
button_frame = tkinter.Frame(frame, bg="#f0f0f0")
button_frame.grid(row=3, column=0, pady=10)

save_button = tkinter.Button(button_frame, text="Save Data", command=save_data, bg="#4CAF50", fg="white")
save_button.grid(row=0, column=0, padx=5)

clear_button = tkinter.Button(button_frame, text="Clear", command=clear_fields, bg="#f44336", fg="white")
clear_button.grid(row=0, column=1, padx=5)

window.mainloop()

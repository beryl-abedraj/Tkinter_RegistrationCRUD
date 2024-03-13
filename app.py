import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="python_db")
cursor = db.cursor()

def create_student():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    gender = entry_gender.get()
    department = selected_department.get()
    year = entry_year.get()
    company = entry_company.get()
    salary = entry_salary.get()
    cursor.execute("INSERT INTO mister (name, email, phone, gender, department, year, company, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, email, phone, gender, department, year, company, salary))
    db.commit()
    messagebox.showinfo("Success", "Student record created successfully.")

def reset_values():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    selected_department.set("Select")
    entry_year.delete(0, tk.END)
    entry_company.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

window = tk.Tk()
window.title("Student Registration")
window.configure(bg="#303030")

label_name = tk.Label(window, text="Name :")
label_name.grid(row=0, column=0, padx=50, pady=25)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)


label_email = tk.Label(window, text="Email :")
label_email.grid(row=1, column=0, padx=50, pady=25)
entry_email = tk.Entry(window)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_phone = tk.Label(window, text="Phone :")
label_phone.grid(row=2, column=0, padx=50, pady=25)
entry_phone = tk.Entry(window)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

label_gender = tk.Label(window, text="Gender :")
label_gender.grid(row=3, column=0, padx=50, pady=25)
entry_gender = tk.Entry(window)
entry_gender.grid(row=3, column=1, padx=10, pady=5)

departments = ["CSE", "MECH", "ECE", "EEE", "AI & DS", "AUTO", "CIVIL", "EIE", "IT"]

selected_department = tk.StringVar(window)
selected_department.set("Select")

label_department = tk.Label(window, text="Department :")
label_department.grid(row=4, column=0, padx=50, pady=25)
dropdown_department = tk.OptionMenu(window, selected_department, *departments)
dropdown_department.grid(row=4, column=1, padx=10, pady=5)

label_year = tk.Label(window, text="Graduated Year :")
label_year.grid(row=5, column=0, padx=50, pady=25)
entry_year = tk.Entry(window)
entry_year.grid(row=5, column=1, padx=10, pady=5)

label_company = tk.Label(window, text="Organization :")
label_company.grid(row=6, column=0, padx=50, pady=25)
entry_company = tk.Entry(window)
entry_company.grid(row=6, column=1, padx=10, pady=5)

label_salary = tk.Label(window, text="Salary in LPA :")
label_salary.grid(row=7, column=0, padx=50, pady=25)
entry_salary = tk.Entry(window)
entry_salary.grid(row=7, column=1, padx=10, pady=5)

button_create = tk.Button(window, text="UPLOAD", command=create_student, bg="#0077b6", fg="#ffffff")
button_create.grid(row=8, column=0, padx=10, pady=5)

button_reset = tk.Button(window, text="RESET", command=reset_values, bg="#0077b6", fg="#ffffff")
button_reset.grid(row=8, column=1, padx=10, pady=5)

window.mainloop()
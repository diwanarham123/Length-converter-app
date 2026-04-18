import tkinter as tk
from tkinter import messagebox

def convert_inches_to_cm():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm", fg='darkgreen')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for inches.")
        result_label.config(text="", fg='red')

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg='#F0F0F0')

label_inches = tk.Label(root, text="Enter length in inches:", font=('Arial', 14), bg='#F0F0F0', fg='#333333')
label_inches.pack(pady=20)

entry_inches = tk.Entry(root, font=('Arial', 14), width=20, bd=2, relief='groove', bg='#FFFFFF')
entry_inches.pack(pady=10)

convert_button = tk.Button(root, text="Convert to CM", font=('Arial', 14, 'bold'), command=convert_inches_to_cm,
                           bg='#4CAF50', fg='white', activebackground='#45a049', activeforeground='white',
                           padx=15, pady=8, bd=0, relief='raised')
convert_button.pack(pady=20)

result_label = tk.Label(root, text="", font=('Arial', 18, 'bold'), bg='#F0F0F0', fg='darkgreen')
result_label.pack(pady=10)

root.mainloop()
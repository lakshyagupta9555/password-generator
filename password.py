import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(password_length.get())  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)  
    password_entry.insert(tk.END, password)
def copy_to_clipboard(): 
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
password_length = tk.Entry(root, width=10)
password_length.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=10)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)
root.mainloop()
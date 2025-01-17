import tkinter as tk
from tkinter import messagebox
import keyboard
from blocked_keys import keys


def block_non_digit_keys():
    for key in keys:
        keyboard.block_key(key)

def check_password():
    with open("password.txt", "r") as file:
        correct_password = file.read().strip()

    entered_password = password_entry.get()
    if entered_password == correct_password:
        messagebox.showinfo("Success", "Password Correct! Unlocking...")
        root.destroy()  # Close the lock screen
    else:
        messagebox.showerror("Error", "Incorrect Password")
        password_entry.delete(0, tk.END)

# Create the lock screen window
root = tk.Tk()
root.attributes("-fullscreen", True) 
root.title("System Locked")
root.configure(bg="black")

# Instruction label
instruction_label = tk.Label(
    root, text="Enter Password to Unlock", font=("Arial", 24), fg="white", bg="black"
)
instruction_label.pack(pady=50)

# Password entry field
password_entry = tk.Entry(root, font=("Arial", 20), show="*", justify="center")
password_entry.pack(ipady=10, ipadx=10)

# Unlock button
unlock_button = tk.Button(
    root, text="Unlock", font=("Arial", 16), command=check_password, bg="gray", fg="white"
)
unlock_button.pack(pady=20)

# Disable keys
block_non_digit_keys()

# Focus the password entry field
password_entry.focus()

# Block interaction with desktop
root.mainloop()

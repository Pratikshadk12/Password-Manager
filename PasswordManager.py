import tkinter as tk
from tkinter import messagebox
import json
import base64
import hashlib
import secrets
import string
import pyperclip
from cryptography.fernet import Fernet

# ---------------- Encryption / Decryption ---------------- #
MASTER_PASSWORD = "mysecret"  # 🔒 Change this for real security
key = hashlib.sha256(MASTER_PASSWORD.encode()).digest()
key = base64.urlsafe_b64encode(key[:32])  # Fernet needs 32-byte key
cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher.decrypt(text.encode()).decode()

# ---------------- Save Password ---------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    new_data = {
        website: {
            "username": username,
            "password": encrypt(password)
        }
    }

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Success", f"Password for {website} saved!")
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ---------------- Find Password ---------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")
        return

    if website in data:
        username = data[website]["username"]
        password = decrypt(data[website]["password"])
        pyperclip.copy(password)  # Copy to clipboard
        messagebox.showinfo(website, f"Username: {username}\nPassword copied to clipboard ✅")
    else:
        messagebox.showerror("Error", f"No details for {website} found.")

# ---------------- Generate Strong Password ---------------- #
def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Automatically copy generated password
    messagebox.showinfo("Password Generated", "Password generated and copied to clipboard ✅")

# ---------------- Tkinter UI ---------------- #
root = tk.Tk()
root.title("🔑 Password Manager")
root.geometry("420x380")
root.resizable(False, False)

# Labels & Entries
tk.Label(root, text="Website:").pack(pady=5)
website_entry = tk.Entry(root, width=30)
website_entry.pack()

tk.Label(root, text="Username/Email:").pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password, bg="orange", fg="black").pack(pady=5)
tk.Button(root, text="Save Password", command=save_password, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Find Password", command=find_password, bg="blue", fg="white").pack(pady=5)

root.mainloop()

# 🔑 Password Manager (Python)

A simple yet powerful **Password Manager** built with **Python and Tkinter GUI**.
It allows you to **store, generate, and retrieve passwords securely** with **AES encryption (Fernet)**.
Perfect for beginners to learn **Python basics**, **file handling**, **encryption**, and **GUI development**.

---

## 🚀 Features

* 📝 **Save Passwords** (Encrypted and stored in `passwords.json`)
* 🔍 **Find Passwords** instantly by website name
* 🔒 **Encrypt & Decrypt** passwords with a master key
* ⚡ **Generate Strong Passwords** (auto-copied to clipboard)
* 📋 **Clipboard Integration** – No need to type manually

---

## 🛠️ Technologies Used

* **Python** (3.x)
* **Tkinter** (for GUI)
* **Cryptography (Fernet)** for encryption
* **Pyperclip** for clipboard support
* **JSON** for local storage

---

## 📁 Folder Structure

```
password-manager/
│
├── src/
│   ├── password_manager.py    # Main Python program
│   ├── passwords.json         # Encrypted saved passwords
│
├── README.md
└── .gitignore
```

---

## 🧩 Setup Instructions (VS Code)

### 1️⃣ Install Required Tools

* [Python 3.x](https://www.python.org/downloads/)
* [VS Code](https://code.visualstudio.com/)
* Install **Python Extension Pack** in VS Code
* [Git](https://git-scm.com/)

---

### 2️⃣ Install Required Libraries

Run in terminal:

```bash
pip install cryptography pyperclip
```

---

### 3️⃣ Verify Installations

```bash
python --version
pip show cryptography
pip show pyperclip
git --version
```

---

## 🖥️ How to Run the Project

### 1️⃣ Create Folder Structure

```
password-manager/
├── src/
```

---

### 2️⃣ Add Code

* Save the given `password_manager.py` file inside the `src/` folder.

---

### 3️⃣ Run the Project

In the terminal, from the **src** folder:

```bash
python password_manager.py
```

---

## ⬆️ How to Push Code to GitHub

### 1️⃣ Create a New Repository on GitHub

* Go to **GitHub → New Repository** → Name: `password-manager`

---

### 2️⃣ Initialize Git and Push

From your project root folder:

```bash
git init
git add .
git commit -m "Initial commit - Password Manager"
git branch -M main
git remote add origin https://github.com/your-username/password-manager.git
git push -u origin main
```

---

## 📌 Future Enhancements

* 🔑 Add Master Password login screen
* 💾 Sync with cloud storage (Google Drive/Dropbox)
* 📱 Build mobile app version with Kivy
* 🌐 Browser extension for autofill

---

## 🙌 Author

Created by **Pratiksha** – 2nd Year AIML Student, Reva University
GitHub: [pratikshadk12](https://github.com/pratikshadk12)

---

## ⚠️ .gitignore Recommendation

Add a `.gitignore` file to exclude sensitive files:

```
# Ignore saved passwords
passwords.json

# Python cache
__pycache__/
*.pyc
```

---

Happy Password Managing! 🔒✨

---

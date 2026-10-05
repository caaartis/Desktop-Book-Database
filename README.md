📚 BookStore App

A simple desktop application for managing and tracking books, built with Python using Tkinter for the graphical user interface and SQLite for the database.

📌 Features

Zero External Dependencies: Built entirely with standard Python libraries (tkinter and sqlite3). Creating a virtual environment (venv) or installing third-party packages via pip is not required.

Automatic Database Initialization: The database file (books.db) will be automatically created on the first run if it does not already exist.

🛠️ Prerequisites

Python 3.x installed on your system.

💡 Note for Linux users (Ubuntu/Debian):
In some Linux distributions, tkinter is packaged separately from Python. If you encounter a ModuleNotFoundError: No module named 'tkinter' error, install it using:

sudo apt-get install python3-tk


📁 Project Structure

- frontend.py — Graphical User Interface (GUI). Main file to run the application.

- backend.py — Database logic and CRUD operations for SQLite (books.db).

- books.db — SQLite database file (generated automatically).

🚀 How to Run
Run the frontend.py file:

Windows:
```bash
python frontend.py
```

macOS / Linux:
```bash
python3 frontend.py
```

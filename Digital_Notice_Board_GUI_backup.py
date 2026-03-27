import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

FILE_NAME = "notices.json"

# Load notices
def load_notices():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save notices
def save_notices(notices):
    with open(FILE_NAME, "w") as file:
        json.dump(notices, file)

# Show notices
def show_notices(notices=None):
    listbox.delete(0, tk.END)
    if notices is None:
        notices = load_notices()
    for n in notices:
        listbox.insert(tk.END, n["title"] + " | " + n["category"] + " | " + n["date"])

# Add Notice
def add_notice():
    title = title_entry.get()
    message = message_entry.get()
    category = category_entry.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    if title == "" or message == "" or category == "":
        messagebox.showerror("Error", "All fields required")
        return

    notices = load_notices()
    notices.append({
        "title": title,
        "message": message,
        "category": category,
        "date": date
    })

    save_notices(notices)
    show_notices()
    title_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

# Delete Notice
def delete_notice():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        notices = load_notices()
        notices.pop(index)
        save_notices(notices)
        show_notices()

# Update Notice
def update_notice():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        notices = load_notices()

        notices[index]["title"] = title_entry.get()
        notices[index]["message"] = message_entry.get()
        notices[index]["category"] = category_entry.get()

        save_notices(notices)
        show_notices()

# Sort by Date
def sort_by_date():
    notices = load_notices()
    notices.sort(key=lambda x: x["date"], reverse=True)
    show_notices(notices)

# Sort by Category
def sort_by_category():
    notices = load_notices()
    notices.sort(key=lambda x: x["category"])
    show_notices(notices)

# GUI Window
root = tk.Tk()
root.title("Digital Notice Board")
root.geometry("600x500")

tk.Label(root, text="Title").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Message").pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root, width=50)
category_entry.pack()

tk.Button(root, text="Add Notice", command=add_notice).pack(pady=5)
tk.Button(root, text="Update Notice", command=update_notice).pack(pady=5)
tk.Button(root, text="Delete Notice", command=delete_notice).pack(pady=5)
tk.Button(root, text="Sort by Date", command=sort_by_date).pack(pady=5)
tk.Button(root, text="Sort by Category", command=sort_by_category).pack(pady=5)

listbox = tk.Listbox(root, width=80)
listbox.pack(pady=10)

show_notices()

root.mainloop()
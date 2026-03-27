import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


notices = []
next_id = 1


def show_notices(display_notices=None):
    listbox.delete(0, tk.END)
    if display_notices is None:
        display_notices = notices
    for n in display_notices:
        listbox.insert(tk.END, f"{n['id']} | {n['title']} | {n['category']} | {n['date']}")


def add_notice():
    global next_id
    title = title_entry.get()
    message = message_entry.get()
    category = category_combo.get()
    
    if not title or not message or category == "Select Category":
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_notice = {
        "id": next_id,
        "title": title,
        "message": message,
        "category": category,
        "date": date
    }
    notices.append(new_notice)
    next_id += 1
    
    title_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    category_combo.set("Select Category")
    
    show_notices()
    messagebox.showinfo("Success", "Notice added!")


def delete_notice():
    id_str = id_entry.get()
    if not id_str:
        messagebox.showerror("Error", "Enter ID")
        return
    try:
        notice_id = int(id_str)
    except ValueError:
        messagebox.showerror("Error", "ID must be number")
        return
    
    for i, n in enumerate(notices):
        if n["id"] == notice_id:
            del notices[i]
            show_notices()
            id_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Notice deleted!")
            return
    messagebox.showerror("Error", f"ID {notice_id} not found")

def update_notice():
    id_str = id_entry.get()
    title = title_entry.get()
    message = message_entry.get()
    category = category_combo.get()
    
    if not id_str or not title or not message or category == "Select Category":
        messagebox.showerror("Error", "Enter ID and fill all fields")
        return
    
    try:
        notice_id = int(id_str)
    except ValueError:
        messagebox.showerror("Error", "ID must be number")
        return
    
    for n in notices:
        if n["id"] == notice_id:
            n["title"] = title
            n["message"] = message
            n["category"] = category
            # Update date? No, keep original
            show_notices()
            title_entry.delete(0, tk.END)
            message_entry.delete(0, tk.END)
            category_combo.set("Select Category")
            id_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Notice updated!")
            return
    messagebox.showerror("Error", f"ID {notice_id} not found")


def search_category():
    cat = category_combo.get()
    if cat == "Select Category":
        show_notices()
        return
    filtered = [n for n in notices if n["category"] == cat]
    show_notices(filtered)


def search_date():
    date_str = message_entry.get()  
    if not date_str:
        show_notices()
        return
    filtered = [n for n in notices if date_str in n["date"]]
    show_notices(filtered)


def clear_search():
    title_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    category_combo.set("Select Category")
    show_notices()


root = tk.Tk()
root.title("Digital Notice Board")
root.geometry("700x600")


tk.Label(root, text="Notice ID:").pack(pady=5)
id_entry = tk.Entry(root, width=10, font=("Arial", 12))
id_entry.pack()


tk.Label(root, text="Title:").pack(pady=5)
title_entry = tk.Entry(root, width=50, font=("Arial", 12))
title_entry.pack()


tk.Label(root, text="Message (or Date for search):").pack(pady=5)
message_entry = tk.Entry(root, width=50, font=("Arial", 12))
message_entry.pack()

tk.Label(root, text="Category:").pack(pady=5)
category_combo = ttk.Combobox(root, values=["Academic", "Event", "Attendance", "General"], state="readonly", width=47)
category_combo.set("Select Category")
category_combo.pack()


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Notice", command=add_notice, bg="lightgreen", fg="darkgreen", font=("Arial", 12, "bold"), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Update Notice", command=update_notice, bg="lightblue", fg="darkblue", font=("Arial", 12, "bold"), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete Notice", command=delete_notice, bg="lightcoral", fg="darkred", font=("Arial", 12, "bold"), width=15).pack(side=tk.LEFT, padx=5)

tk.Button(btn_frame, text="Search Category", command=search_category, bg="orange", fg="black", font=("Arial", 12, "bold"), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Search Date", command=search_date, bg="orange", fg="black", font=("Arial", 12, "bold"), width=15).pack(side=tk.LEFT, padx=5)

tk.Button(root, text="Clear All", command=clear_search, bg="lightgray", font=("Arial", 12)).pack(pady=5)

tk.Label(root, text="Notices (ID | Title | Category | Date):", font=("Arial", 14, "bold")).pack(pady=10)
listbox = tk.Listbox(root, width=90, height=15, font=("Arial", 11))
listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

show_notices()

root.mainloop()


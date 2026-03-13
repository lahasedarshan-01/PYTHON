import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# ---------------- DATABASE ----------------

conn = sqlite3.connect("notice_board.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

CATEGORIES = ["Academic", "Event", "General", "Notice", "Examination"]


class NoticeBoard(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Digital Notice Board")
        self.geometry("950x650")
        self.show_main_menu()

    # ---------------- MAIN MENU ----------------
    def show_main_menu(self):
        self.clear()

        ctk.CTkLabel(self, text="Digital Notice Board", font=("Arial", 26)).pack(pady=20)

        ctk.CTkButton(self, text="Admin Panel", width=200,
                      command=self.admin_panel).pack(pady=10)

        ctk.CTkButton(self, text="User Panel", width=200,
                      command=self.user_panel).pack(pady=10)

    # ---------------- ADMIN PANEL ----------------
    def admin_panel(self):
        self.clear()

        ctk.CTkLabel(self, text="Admin Panel", font=("Arial", 22)).pack(pady=10)

        self.title_entry = ctk.CTkEntry(self, placeholder_text="Title", width=600, height=40)
        self.title_entry.pack(pady=5)

        self.content_entry = ctk.CTkTextbox(self, width=700, height=120)
        self.content_entry.pack(pady=5)

        self.category_var = ctk.StringVar(value=CATEGORIES[0])
        ctk.CTkOptionMenu(self, values=CATEGORIES,
                          variable=self.category_var, width=300).pack(pady=5)

        self.id_entry = ctk.CTkEntry(self,
                                     placeholder_text="Enter Notice ID for Update/Delete",
                                     width=400, height=35)
        self.id_entry.pack(pady=5)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Add Notice", width=150,
                      fg_color="green", hover_color="#006400",
                      command=self.add_notice).grid(row=0, column=0, padx=10, pady=5)

        ctk.CTkButton(button_frame, text="Update Notice", width=150,
                      command=self.update_notice).grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkButton(button_frame, text="Delete Notice", width=150,
                      fg_color="red", hover_color="#8B0000",
                      command=self.delete_notice).grid(row=0, column=2, padx=10, pady=5)

        ctk.CTkButton(button_frame, text="Back", width=150,
                      fg_color="blue", hover_color="#00008B",
                      command=self.show_main_menu).grid(row=1, column=0, padx=10, pady=5)

        # ---- Notice List for Admin ----
        ctk.CTkLabel(self, text="All Notices", font=("Arial", 18)).pack(pady=5)

        self.admin_notice_box = ctk.CTkTextbox(self, width=900, height=200)
        self.admin_notice_box.pack(pady=10)

        self.load_admin_notices()

    def load_admin_notices(self):
        self.admin_notice_box.delete("1.0", "end")
        cursor.execute("SELECT * FROM notices ORDER BY created_at DESC")
        data = cursor.fetchall()

        for n in data:
            self.admin_notice_box.insert("end",
                f"ID: {n[0]} | {n[1]} | {n[3]} | {n[4]}\n")

    # ---------------- ADMIN FUNCTIONS ----------------
    def add_notice(self):
        cursor.execute("INSERT INTO notices(title,content,category) VALUES(?,?,?)",
                       (self.title_entry.get(),
                        self.content_entry.get("1.0", "end"),
                        self.category_var.get()))
        conn.commit()
        messagebox.showinfo("Success", "Notice Added")
        self.admin_panel()

    def update_notice(self):
        cursor.execute("""
        UPDATE notices
        SET title=?, content=?, category=?
        WHERE id=?
        """, (self.title_entry.get(),
              self.content_entry.get("1.0", "end"),
              self.category_var.get(),
              self.id_entry.get()))
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Wrong ID Entered")
        else:
            messagebox.showinfo("Success", "Notice Updated")
            self.admin_panel()

    def delete_notice(self):
        cursor.execute("DELETE FROM notices WHERE id=?",
                       (self.id_entry.get(),))
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Wrong ID Entered")
        else:
            messagebox.showinfo("Success", "Notice Deleted")
            self.admin_panel()

    # ---------------- USER PANEL ----------------
    def user_panel(self):
        self.clear()

        ctk.CTkLabel(self, text="User Panel", font=("Arial", 22)).pack(pady=10)

        self.sort_var = ctk.StringVar(value="Date")
        ctk.CTkOptionMenu(self, values=["Date", "Category"],
                          variable=self.sort_var).pack(pady=5)

        self.filter_var = ctk.StringVar(value="All")
        filter_options = ["All"] + CATEGORIES
        ctk.CTkOptionMenu(self, values=filter_options,
                          variable=self.filter_var).pack(pady=5)

        ctk.CTkButton(self, text="View Notices",
                      command=self.view_notices).pack(pady=5)

        self.notice_box = ctk.CTkTextbox(self, width=900, height=350)
        self.notice_box.pack(pady=10)

        ctk.CTkButton(self, text="Back",
                      fg_color="blue", hover_color="#00008B",
                      command=self.show_main_menu).pack(pady=5)

    def view_notices(self):
        self.notice_box.delete("1.0", "end")

        query = "SELECT * FROM notices"
        params = []

        if self.filter_var.get() != "All":
            query += " WHERE category=?"
            params.append(self.filter_var.get())

        if self.sort_var.get() == "Date":
            query += " ORDER BY created_at DESC"
        else:
            query += " ORDER BY category ASC"

        cursor.execute(query, params)
        data = cursor.fetchall()

        for n in data:
            self.notice_box.insert("end",
                f"ID: {n[0]}\nTitle: {n[1]}\nCategory: {n[3]}\nDate: {n[4]}\n{n[2]}\n{'-'*60}\n")

    # ---------------- CLEAR ----------------
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = NoticeBoard()
    app.mainloop()
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

# Add Notice
def add_notice():
    title = input("Enter Notice Title: ")
    message = input("Enter Notice Message: ")
    category = input("Enter Category (Exam/Event/General): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    notices = load_notices()
    notices.append({
        "title": title,
        "message": message,
        "category": category,
        "date": date
    })

    save_notices(notices)
    print("Notice Added Successfully!\n")

# View Notices
def view_notices():
    notices = load_notices()
    if not notices:
        print("No Notices Found\n")
        return

    print("\nAll Notices:")
    for i, n in enumerate(notices):
        print(i+1, n["title"], "-", n["category"], "-", n["date"])
        print(" ", n["message"])
    print()

# Delete Notice
def delete_notice():
    notices = load_notices()
    view_notices()

    num = int(input("Enter notice number to delete: "))
    if 0 < num <= len(notices):
        notices.pop(num-1)
        save_notices(notices)
        print("Notice Deleted\n")
    else:
        print("Invalid Number\n")

# Update Notice
def update_notice():
    notices = load_notices()
    view_notices()

    num = int(input("Enter notice number to update: "))
    if 0 < num <= len(notices):
        title = input("Enter New Title: ")
        message = input("Enter New Message: ")
        category = input("Enter New Category: ")

        notices[num-1]["title"] = title
        notices[num-1]["message"] = message
        notices[num-1]["category"] = category

        save_notices(notices)
        print("Notice Updated\n")
    else:
        print("Invalid Number\n")

# Sort by Date
def sort_by_date():
    notices = load_notices()
    notices.sort(key=lambda x: x["date"], reverse=True)

    print("\nNotices Sorted by Date:")
    for n in notices:
        print(n["title"], "-", n["date"])
        print(n["message"])
    print()

# Sort by Category
def sort_by_category():
    notices = load_notices()
    notices.sort(key=lambda x: x["category"])

    print("\nNotices Sorted by Category:")
    for n in notices:
        print(n["title"], "-", n["category"])
        print(n["message"])
    print()

# Main Menu
while True:
    print("------ Digital Notice Board ------")
    print("1. Add Notice")
    print("2. View Notices")
    print("3. Update Notice")
    print("4. Delete Notice")
    print("5. Sort Notices by Date")
    print("6. Sort Notices by Category")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_notice()
    elif choice == "2":
        view_notices()
    elif choice == "3":
        update_notice()
    elif choice == "4":
        delete_notice()
    elif choice == "5":
        sort_by_date()
    elif choice == "6":
        sort_by_category()
    elif choice == "7":
        break
    else:
        print("Invalid Choice\n")
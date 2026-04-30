import tkinter as tk
from tkinter import messagebox

from database import (
    create_table,
    add_suggestion,
    get_all_suggestions,
    get_new_suggestions,
    update_suggestion_status
)

from services import VALID_CATEGORIES, VALID_URGENCY, VALID_STATUSES


create_table()


def submit_suggestion():
    text = suggestion_text.get("1.0", tk.END).strip()
    category = category_var.get()
    urgency = urgency_var.get()

    if not text:
        messagebox.showerror("Error", "Suggestion cannot be empty.")
        return

    add_suggestion(text, category, urgency)
    suggestion_text.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Suggestion submitted successfully.")
    view_all_suggestions()


def display_suggestions(suggestions):
    output_box.delete("1.0", tk.END)

    if not suggestions:
        output_box.insert(tk.END, "No suggestions found.")
        return

    for item in suggestions:
        suggestion_id, text, category, urgency, status, priority = item

        output_box.insert(tk.END, f"ID: {suggestion_id}\n")
        output_box.insert(tk.END, f"Text: {text}\n")
        output_box.insert(tk.END, f"Category: {category}\n")
        output_box.insert(tk.END, f"Urgency: {urgency}\n")
        output_box.insert(tk.END, f"Status: {status}\n")
        output_box.insert(tk.END, f"Priority: {priority}\n")
        output_box.insert(tk.END, "-" * 40 + "\n")


def view_all_suggestions():
    display_suggestions(get_all_suggestions())


def view_new_suggestions():
    display_suggestions(get_new_suggestions())


def update_status():
    try:
        suggestion_id = int(update_id_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid suggestion ID.")
        return

    new_status = status_var.get()
    update_suggestion_status(suggestion_id, new_status)

    messagebox.showinfo("Success", "Status updated successfully.")
    view_all_suggestions()


window = tk.Tk()
window.title("Anonymous Suggestions Box")
window.geometry("700x650")

title = tk.Label(window, text="Anonymous Suggestions Box", font=("Arial", 18, "bold"))
title.pack(pady=10)

tk.Label(window, text="Enter suggestion:").pack()
suggestion_text = tk.Text(window, height=5, width=70)
suggestion_text.pack(pady=5)

tk.Label(window, text="Category:").pack()
category_var = tk.StringVar(value=VALID_CATEGORIES[0])
category_menu = tk.OptionMenu(window, category_var, *VALID_CATEGORIES)
category_menu.pack()

tk.Label(window, text="Urgency:").pack()
urgency_var = tk.StringVar(value=VALID_URGENCY[0])
urgency_menu = tk.OptionMenu(window, urgency_var, *VALID_URGENCY)
urgency_menu.pack()

submit_button = tk.Button(window, text="Submit Suggestion", command=submit_suggestion)
submit_button.pack(pady=10)

tk.Button(window, text="View All Suggestions", command=view_all_suggestions).pack(pady=3)
tk.Button(window, text="View New Suggestions", command=view_new_suggestions).pack(pady=3)

tk.Label(window, text="Update suggestion status").pack(pady=10)

tk.Label(window, text="Suggestion ID:").pack()
update_id_entry = tk.Entry(window)
update_id_entry.pack()

status_var = tk.StringVar(value=VALID_STATUSES[0])
status_menu = tk.OptionMenu(window, status_var, *VALID_STATUSES)
status_menu.pack()

tk.Button(window, text="Update Status", command=update_status).pack(pady=10)

tk.Label(window, text="Suggestions:").pack()
output_box = tk.Text(window, height=15, width=80)
output_box.pack(pady=5)

view_all_suggestions()

window.mainloop()
import tkinter as tk
from tkinter import messagebox

def generate_password():
    website_name = website_entry.get()
    action = action_entry.get()
    device = device_entry.get()
    
    if not website_name or not action or not device:
        messagebox.showerror("Input Error", "All fields must be filled!")
        return
    
    password_string = "".join([letter for letter in website_name if letter.lower() not in "aeiou"])[:2].upper()
    site_abbreviation = password_string
    letters_in_site_name = str(len(website_name))
    verb = "".join([letter for letter in action if letter.lower() not in "aeiou"]).lower().replace(" ", "")
    subject = device.upper().replace(" ", "")
    
    specials = ""
    letter = website_name[0].lower()
    if letter in "abcd":
        specials = "!@"
    elif letter in "efgh":
        specials = "#$"
    elif letter in "ijkl":
        specials = "%^"
    elif letter in "mnop":
        specials = "&*"
    else:
        specials = "()"
    
    password = site_abbreviation + letters_in_site_name + verb + subject + specials
    result_label.config(text=f'Your password: {password}', fg="green")

# UI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Website Name:", bg="#f0f0f0").pack(pady=5)
website_entry = tk.Entry(root, width=30)
website_entry.pack()

tk.Label(root, text="Action:", bg="#f0f0f0").pack(pady=5)
action_entry = tk.Entry(root, width=30)
action_entry.pack()

tk.Label(root, text="Device:", bg="#f0f0f0").pack(pady=5)
device_entry = tk.Entry(root, width=30)
device_entry.pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()

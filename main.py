from tkinter import *
from tkinter import messagebox
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + [random.choice(symbols)
                                                                              for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_text.insert(0,string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website)== 0 or len(password) == 0:
        is_empty = messagebox.showerror(title="Missing Value", message="You have some empty values.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_text.delete(0,END)
            password_text.delete(0,END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = website_text.get()
    try:
        with open("data.json", "r") as data:
            data = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file is found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website}", message= f"Email: {email}\n Password: f{password}")
        else:
            messagebox.showerror(title=f"{website}", message="No data for this website.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# #labels
website= Label(text="Website:")
website.grid(column=0, row=1)
email= Label(text="Username/Email:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries
website_text = Entry(width=21)
website_text.grid(column=1, row=1, columnspan=1)
website_text.focus()
email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0,string="trohit920@gmail.com")
password_text = Entry(width=21)
password_text.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)
add = Button(text="Add", width=36, command=save_password)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", command=search_password, width=13)
search.grid(column=2, row=1)
window.mainloop()
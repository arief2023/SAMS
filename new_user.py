import sqlite3
from tkinter import *
from tkinter import messagebox
import re

room_number_taken = []


class NewUser:

    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("New Admin User Sign Up!")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        self.top = Frame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")

        # The title display
        self.label = Label(self.top, font=('Bookman Old Style', 50, 'bold'), text="Enter Details", fg="#993333",
                           anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # name
        self.name_label = Label(self.bottom, font=('Bookman Old Style', 20, 'bold'), text="Admin Name: ", fg="#993333",
                                anchor="w")
        self.name_label.grid(row=0, column=2, padx=10, pady=(70, 0))

        # text entry for name
        self.name_var = StringVar()
        self.name_entry = Entry(self.bottom, width=30, textvar=self.name_var, font="14")
        self.name_entry.grid(row=0, column=3, padx=10, pady=(70, 0))

        # address
        self.address_label = Label(self.bottom, font=('Bookman Old Style', 20, 'bold'), text="Address:", fg="#993333",
                                   anchor="w")
        self.address_label.grid(row=1, column=2, padx=(10, 0), pady=10)  # Adjusted padx

        # text entry for address
        self.address_var = StringVar()
        self.address_entry = Entry(self.bottom, width=30, textvar=self.address_var, font="14")
        self.address_entry.grid(row=1, column=3, padx=10, pady=10)

        # email
        self.email_label = Label(self.bottom, font=('Bookman Old Style', 20, 'bold'), text="E-mail:", fg="#993333",
                                 anchor="w")
        self.email_label.grid(row=2, column=2, padx=(10, 0), pady=10)  # Adjusted padx

        # text entry for email
        self.email_var = StringVar()
        self.email_entry = Entry(self.bottom, width=30, textvar=self.email_var, font="14")
        self.email_entry.grid(row=2, column=3, padx=10, pady=10)

        # mobile number
        self.mobile_label = Label(self.bottom, font=('Bookman Old Style', 20, 'bold'), text="Mobile Number:",
                                  fg="#993333", anchor="w")
        self.mobile_label.grid(row=3, column=2, padx=10, pady=10)

        # text entry field for mobile number
        self.mobile_var = IntVar()
        self.mobile_entry = Entry(self.bottom, width=30, text=self.mobile_var, font="14")
        self.mobile_entry.grid(row=3, column=3, padx=10, pady=10)

        # Password Label
        self.password_label = Label(self.bottom, font=('Bookman Old Style', 20, 'bold'), text="Password:",
                                  fg="#993333", anchor="w")
        self.password_label.grid(row=4, column=2, padx=10, pady=10)

        # text entry field for Password
        self.password_var = IntVar()
        self.password_entry = Entry(self.bottom, width=30, text=self.password_var, font="14")
        self.password_entry.grid(row=4, column=3, padx=10, pady=10)

        # Submit info activity
        def submit_info():
            username = self.name_entry.get()
            address = self.address_entry.get()
            mobile = self.mobile_entry.get()
            email = self.email_entry.get()
            password = self.password_entry.get()

            # Validate mobile and days
            while True:
                self.h = str(self.mobile_entry.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    mobile = self.h
                    ans = True
                    break
                else:
                    ans = False
                    messagebox.showerror("ERROR",
                                         "The mobile number you entered is either not valid or does not have 10 digits.",
                                         parent=self.root)
                    break

            # Validate email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showerror("ERROR", "Invalid email address.", parent=self.root)
                return

            if ans:
                conn = sqlite3.connect('school.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('CREATE TABLE IF NOT EXISTS administrators (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                                   'username TEXT NOT NULL, address TEXT, email TEXT, mobile_number NUMBER, password NUMBER)')

                    # Check if the entry already exists
                    cursor.execute('SELECT * FROM administrators WHERE username=? AND password=? AND email=?',
                                   (username, password, email))
                    existing_entry = cursor.fetchone()

                    if existing_entry:
                        messagebox.showerror("ERROR", "Data for this admin already exists.", parent=self.root)
                    else:
                        cursor.execute('INSERT INTO administrators (username, address, email, mobile_number, password) '
                                       'VALUES (?, ?, ?, ?, ?)', (username, address, email, mobile, password))
                        conn.commit()
                        messagebox.showinfo("Success", "Data submitted successfully!", parent=self.root)
                        # For testing purposes
                        print(cursor.fetchall())

        def reset():
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, "")

            self.mobile_entry.delete(0, END)
            self.mobile_entry.insert(0, "")

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, "")

            self.email_entry.delete(0, END)
            self.email_entry.insert(0, "")

            self.password_entry.delete(0, END)
            self.password_entry.insert(0, "")

        # da submit button
        self.submit_button = Button(self.checkbox, text="Submit", font=('Bookman Old Style', 15), bg="#993333",
                                    relief=RIDGE, height=2, width=15, fg="white", anchor="center", command=submit_info)
        self.submit_button.grid(row=7, column=1, padx=10, pady=10)  # Adjusted row

        # back to home page
        self.back_home_button = Button(self.checkbox, text="Home", font=('Bookman Old Style', 15), bg="#993333",
                                       relief=RIDGE, height=2, width=15, fg="white", anchor="center",
                                       command=self.root.destroy)
        self.back_home_button.grid(row=7, column=2, padx=10, pady=10)  # Adjusted row

        # Da Reset button
        Button(self.checkbox, text="Reset", font=('Bookman Old Style', 15), bg="#993333", relief=RIDGE, height=2,
               width=15, fg="white", anchor="center", command=reset).grid(row=7, column=3)


def new_user_ui():
    root = Tk()
    application = NewUser(root)
    root.mainloop()


# For testing
if __name__ == "__main__":
    new_user_ui()


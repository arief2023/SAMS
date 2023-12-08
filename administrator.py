import sqlite3
from tkinter import *
from tkinter import Toplevel


class Administrator:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Admin Page")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root)
        info_frame.pack(side="top")

        # Display message
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Admin Page", fg="#993333",
                           anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # Add buttons
        btn_add_admin = Button(bottom, text="Add Administrator", font=('Arial', 14), bg='#993333',
                               height=1, width=40, fg='white', anchor="center", command=self.add_administrator)
        btn_add_admin.grid(row=2, column=0, padx=10, pady=(70, 10))

        btn_remove_admin = Button(bottom, text="Remove Administrator", font=('Arial', 14), bg='#993333',
                                  height=1, width=40, fg='white', anchor="center", command=self.remove_administrator)
        btn_remove_admin.grid(row=3, column=0, padx=10, pady=10)

        btn_add_instructor = Button(bottom, text="Add Instructor", font=('Arial', 14), bg='#993333',
                                    height=1, width=40, fg='white', anchor="center", command=self.add_instructor)
        btn_add_instructor.grid(row=4, column=0, padx=10, pady=10)

        btn_remove_instructor = Button(bottom, text="Remove Instructor", font=('Arial', 14), bg='#993333',
                                       height=1, width=40, fg='white', anchor="center", command=self.remove_instructor)
        btn_remove_instructor.grid(row=5, column=0, padx=10, pady=10)

        btn_add_student = Button(bottom, text="Add Student", font=('Arial', 14), bg='#993333',
                                 height=1, width=40, fg='white', anchor="center", command=self.add_student)
        btn_add_student.grid(row=6, column=0, padx=10, pady=10)

        btn_remove_student = Button(bottom, text="Remove Student", font=('Arial', 14), bg='#993333',
                                    height=1, width=40, fg='white', anchor="center", command=self.remove_student)
        btn_remove_student.grid(row=7, column=0, padx=10, pady=10)

        # Create home button
        self.home_button = Button(bottom, text="Home", font=('Bookman Old Style', 15), bg="#993333",
                                  height=1, width=20, fg="white", anchor="center", command=self.go_to_home)
        self.home_button.grid(row=8, column=0, padx=10, pady=(10, 20))

        # Connect to the SQLite database
        self.conn = sqlite3.connect("school.db")
        self.cursor = self.conn.cursor()

        # Create the tables if they do not exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS administrators (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT NOT NULL,
                               address TEXT NOT NULL,
                               email TEXT NOT NULL,
                               mobile_number TEXT NOT NULL,
                               password TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS instructors (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT NOT NULL,
                               password TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT NOT NULL,
                               password TEXT NOT NULL)''')

        # Commit the changes
        self.conn.commit()

    def add_administrator(self):
        # Create a new Toplevel window for user input
        input_window = Toplevel(self.root)

        # Create Entry widgets for details
        username_label = Label(input_window, text="Enter Username:")
        username_label.pack()
        username_entry = Entry(input_window)
        username_entry.pack()

        address_label = Label(input_window, text="Enter Address:")
        address_label.pack()
        address_entry = Entry(input_window)
        address_entry.pack()

        email_label = Label(input_window, text="Enter Email:")
        email_label.pack()
        email_entry = Entry(input_window)
        email_entry.pack()

        mobile_number_label = Label(input_window, text="Enter Mobile Number:")
        mobile_number_label.pack()
        mobile_number_entry = Entry(input_window)
        mobile_number_entry.pack()

        password_label = Label(input_window, text="Enter Password:")
        password_label.pack()
        password_entry = Entry(input_window, show="")  # Use show="" to hide the password
        password_entry.pack()

        # Functionality to add administrator to SQLite database
        def add_admin():
            # Get details from Entry widgets
            username = username_entry.get()
            address = address_entry.get()
            email = email_entry.get()
            mobile_number = mobile_number_entry.get()
            password = password_entry.get()

            # Check if details are not empty
            if username and address and email and mobile_number and password:
                # Execute a query to add an administrator
                self.cursor.execute(
                    "INSERT INTO administrators (username, address, email, mobile_number, password) VALUES (?, ?, ?, ?, ?)",
                    (username, address, email, mobile_number, password))
                # Commit the changes
                self.conn.commit()

                # Close the Toplevel window after adding administrator
                input_window.destroy()

        # Add a button to submit the form
        submit_button = Button(input_window, text="Submit", command=add_admin)
        submit_button.pack()

        # Add an event handler to close the Toplevel window on pressing Enter
        input_window.bind("<Return>", lambda event=None: add_admin())

        # Focus on the username entry widget
        username_entry.focus_set()

        # Add an event handler to prevent closing the Toplevel window
        input_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def remove_administrator(self):
        # Create a new Toplevel window for user input
        input_window = Toplevel(self.root)

        # Ask for username and password
        username_label = Label(input_window, text="Enter Username:")
        username_label.pack()
        username_entry = Entry(input_window)
        username_entry.pack()

        password_label = Label(input_window, text="Enter Password:")
        password_label.pack()
        password_entry = Entry(input_window, show="*")  # Use show="" to hide the password
        password_entry.pack()

        def confirm_removal():
            # Get username and password from Entry widgets
            username = username_entry.get()
            password = password_entry.get()

            # Execute the DELETE query
            self.cursor.execute("DELETE FROM administrators WHERE username = ? AND password = ?", (username, password))

            # Commit the changes
            self.conn.commit()

            # Close the Toplevel window after removing administrator
            input_window.destroy()

        # Add a button to confirm the removal
        confirm_button = Button(input_window, text="Confirm Removal", command=confirm_removal)
        confirm_button.pack()

        # Add an event handler to close the Toplevel window on pressing Enter
        input_window.bind("<Return>", lambda event=None: confirm_removal())

        # Focus on the username entry widget
        username_entry.focus_set()

        # Add an event handler to prevent closing the Toplevel window
        input_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def add_instructor(self):
        input_window = Toplevel(self.root)

        # Create Entry widgets for details
        username_label = Label(input_window, text="Enter Username:")
        username_label.pack()
        username_entry = Entry(input_window)
        username_entry.pack()

        password_label = Label(input_window, text="Enter Password:")
        password_label.pack()
        password_entry = Entry(input_window, show="")  # Use show="" to hide the password
        password_entry.pack()

        # Functionality to add instructor to SQLite database
        def add_instructor():
            # Get details from Entry widgets
            username = username_entry.get()
            password = password_entry.get()

            # Check if details are not empty
            if username and password:

                self.cursor.execute(
                    "INSERT INTO instructors (username, password) VALUES (?, ?)",
                    (username, password))
                # Commit the changes
                self.conn.commit()

                input_window.destroy()

        # Add a button to submit the form
        submit_button = Button(input_window, text="Submit", command=add_instructor)
        submit_button.pack()

        # Add an event handler to close the Toplevel window on pressing Enter
        input_window.bind("<Return>", lambda event=None: add_instructor())

        # Focus on the username entry widget
        username_entry.focus_set()

        # Add an event handler to prevent closing the Toplevel window
        input_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def remove_instructor(self):
        # Create a new Toplevel window for user input
        input_window = Toplevel(self.root)

        # Ask for username and password
        username_label = Label(input_window, text="Enter Username:")
        username_label.pack()
        username_entry = Entry(input_window)
        username_entry.pack()

        password_label = Label(input_window, text="Enter Password:")
        password_label.pack()
        password_entry = Entry(input_window, show="*")  # Use show="" to hide the password
        password_entry.pack()

        def confirm_removal():
            # Get username and password from Entry widgets
            username = username_entry.get()
            password = password_entry.get()

            # Execute the DELETE query
            self.cursor.execute("DELETE FROM instructors WHERE username = ? AND password = ?", (username, password))

            # Commit the changes
            self.conn.commit()

            # Close the Toplevel window after removing instructor
            input_window.destroy()

        # Add a button to confirm the removal
        confirm_button = Button(input_window, text="Confirm Removal", command=confirm_removal)
        confirm_button.pack()

        # Add an event handler to close the Toplevel window on pressing Enter
        input_window.bind("<Return>", lambda event=None: confirm_removal())

        # Focus on the username entry widget
        username_entry.focus_set()

        # Add an event handler to prevent closing the Toplevel window
        input_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def add_student(self):
        # Create a new Toplevel window for user input
        input_window = Toplevel(self.root)

        # Create Entry widgets for details
        username_label = Label(input_window, text="Enter Username:")
        username_label.pack()
        username_entry = Entry(input_window)
        username_entry.pack()

        password_label = Label(input_window, text="Enter Password:")
        password_label.pack()
        password_entry = Entry(input_window, show="*")  # Use show="" to hide the password
        password_entry.pack()

        # Functionality to add administrator to SQLite database
        def add_st():
            # Get details from Entry widgets
            username = username_entry.get()
            password = password_entry.get()

            # Check if details are not empty
            if username and password:
                # Execute a query to add an administrator
                self.cursor.execute(
                    "INSERT INTO students (username, password) VALUES (?, ?)",
                    (username, password))
                # Commit the changes
                self.conn.commit()

                # Close the Toplevel window after adding administrator
                input_window.destroy()

        # Add a button to submit the form
        submit_button = Button(input_window, text="Submit", command=add_st)
        submit_button.pack()

        # Add an event handler to close the Toplevel window on pressing Enter
        input_window.bind("<Return>", lambda event=None: add_st())

        # Focus on the username entry widget
        username_entry.focus_set()

        # Add an event handler to prevent closing the Toplevel window
        input_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def remove_student(self):
        # Create a new Toplevel window for user input
        input_window = Toplevel(self.root)

        # Ask for username and password
        username_label = Label(input_window, text="Enter Username:")
        username_label.pack()
        username_entry = Entry(input_window)
        username_entry.pack()

        password_label = Label(input_window, text="Enter Password:")
        password_label.pack()
        password_entry = Entry(input_window, show="*")  # Use show="" to hide the password
        password_entry.pack()

        def confirm_removal():
            # Get username and password from Entry widgets
            username = username_entry.get()
            password = password_entry.get()

            # Execute the DELETE query
            self.cursor.execute("DELETE FROM students WHERE username = ? AND password = ?", (username, password))

            # Commit the changes
            self.conn.commit()

            input_window.destroy()

        # Add a button to confirm the removal
        confirm_button = Button(input_window, text="Confirm Removal", command=confirm_removal)
        confirm_button.pack()

        # Add an event handler to close the Toplevel window on pressing Enter
        input_window.bind("<Return>", lambda event=None: confirm_removal())

        # Focus on the username entry widget
        username_entry.focus_set()

        # Add an event handler to prevent closing the Toplevel window
        input_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def go_to_home(self):
        # Create a new instance of Administrator to go back to the home page
        new_instance = Administrator(Tk())
        self.root.destroy()


def administrator_ui():
    root = Tk()
    application = Administrator(root)
    root.mainloop()


if __name__ == '__main__':
    administrator_ui()

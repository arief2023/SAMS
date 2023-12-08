import sqlite3
from tkinter import *
from tkinter import simpledialog, messagebox

import new_user
import administrator
import instructor
import student
import about


class Main:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("School Attendance System")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('Bookman Old Style', 25, 'bold'),
                           text="Welcome to School Attendance Management System!", fg="#993333",
                           anchor="center")
        self.label.grid(row=0, column=0, pady=(10, 30))

        # Image
        img = PhotoImage(file="./images/sam.png")
        img_label = Label(bottom, image=img)
        img_label.image = img
        img_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Login label
        self.label = Label(bottom, font=('Bookman Old Style', 20, 'bold'),
                           text="Login As", fg="#993333",
                           anchor="center")
        self.label.grid(row=2, column=0, pady=(10, 30))

        # admin button
        self.admin_button = Button(bottom, text="Administrator", font=('Arial', 14), bg="#993333",
                                   relief=RIDGE, height=1, width=40, fg="white", anchor="center",
                                   command=lambda: self.login("administrator"))
        self.admin_button.grid(row=3, column=0, padx=10, pady=10)

        # instructor button
        self.instructor_button = Button(bottom, text="Instructor", font=('Arial', 14), bg="#993333",
                                        relief=RIDGE, height=1, width=40, fg="white", anchor="center",
                                        command=lambda: self.login("instructor"))
        self.instructor_button.grid(row=4, column=0, padx=10, pady=10)

        # student button
        self.student_button = Button(bottom, text="Student", font=('Arial', 14), bg="#993333",
                                     relief=RIDGE, height=1, width=40, fg="white", anchor="center",
                                     command=lambda: self.login("student"))
        self.student_button.grid(row=5, column=0, padx=10, pady=10)

        # button to add new admin if the database is empty
        self.login_label = Button(bottom, text="New Admin: Sign Up", font=('Arial', 14), bg="#993333",
                                  relief=RIDGE, height=1, width=40, fg="white", anchor="center",
                                  command=new_user.new_user_ui)
        self.login_label.grid(row=6, column=0, padx=10, pady=10)

        # button to view the about page
        self.about_button = Button(bottom, text='About', font=('Arial', 14), bg='#993333',
                                   height=1, width=30, fg="white", anchor="center", command=about.about_ui)
        self.about_button.grid(row=7, column=0, padx=10, pady=10)

    def login(self, role):
        username = simpledialog.askstring(f"{role.capitalize()} Login", "Enter Username:")
        password = simpledialog.askstring(f"{role.capitalize()} Login", "Enter Password:")

        user_role = self.verify_user(username, password, role)

        if user_role:
            print(f"Login successful as {role.capitalize()}")
            # Redirect based on the user role
            if user_role == "administrator":
                administrator.administrator_ui()
            elif user_role == "instructor":
                instructor.instructor_ui()
            elif user_role == "student":
                student.student_ui()
        else:
            messagebox.showinfo("Login failed", "Invalid username or password.!", parent=self.root)

    def verify_user(self, username, password, role):
        # Connect to the SQLite database
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Execute a query to verify the user's credentials and get the role
        cursor.execute(f"SELECT * FROM {role}s WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        # Close the database connection
        conn.close()

        return role if result else None


def home_ui():
    root = Tk()
    application = Main(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()

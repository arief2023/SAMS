# student.py

from tkinter import *
from tkinter import simpledialog, messagebox
from instructor import AttendanceStatus


class Student:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Student Info")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="left")

        # display title
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Student Page", fg="#993333",
                           anchor="center")
        self.label.grid(row=0, column=0, padx=10, pady=(10, 70), columnspan=2)

        # Entry fields for username and password
        self.username_label = Label(bottom, text="Username:", font=('Arial', 14))
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = Entry(bottom, font=('Arial', 14))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = Label(bottom, text="Password:", font=('Arial', 14))
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = Entry(bottom, show="*", font=('Arial', 14))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to view attendance report
        view_report = Button(bottom, text="View Attendance Report", font=('Arial', 20), bg="#993333",
                             relief=RIDGE, height=2, width=30, fg="white", anchor="center",
                             command=self.view_attendance_report)
        view_report.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # create home button
        self.home_button = Button(bottom, text="Home", font=('Arial', 15), bg="#993333",
                                  height=2, width=20, fg="white", anchor="center", command=self.root.destroy)
        self.home_button.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 20))

        # Initialize the AttendanceStatus class
        self.attendance_status = AttendanceStatus()

    def view_attendance_report(self):
        # Retrieve username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        report = self.attendance_status.view_student_attendance_report(username)

        # Display the report in a new window
        report_window = Toplevel(self.root)
        report_window.title("Attendance Report")

        report_label = Label(report_window, text=f"Attendance Report for {username}", font=('Arial', 16, 'bold'))
        report_label.pack()

        for row in report:
            row_label = Label(report_window, text=row)
            row_label.pack()


def student_ui():
    root = Tk()
    application = Student(root)
    root.mainloop()


# For testing
if __name__ == "__main__":
    student_ui()

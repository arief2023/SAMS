import sqlite3
from tkinter import *
from tkinter import simpledialog, messagebox


class AttendanceStatus:
    def __init__(self):
        self.conn = sqlite3.connect("school.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT NOT NULL,
                               status TEXT NOT NULL,
                               date TEXT NOT NULL)''')
        self.conn.commit()

    def mark_attendance(self, username, status, date):
        self.cursor.execute("INSERT INTO attendance (username, status, date) VALUES (?, ?, ?)",
                            (username, status, date))
        self.conn.commit()

    def view_attendance_report(self):
        self.cursor.execute("SELECT * FROM attendance")
        rows = self.cursor.fetchall()
        return rows

    def view_student_attendance_report(self, student_name):
        self.cursor.execute("SELECT * FROM attendance WHERE username = ?", (student_name,))
        rows = self.cursor.fetchall()
        return rows

    def generate_report(self):
        # Retrieve data from the 'attendance' table
        self.cursor.execute('SELECT * FROM attendance')
        rows = self.cursor.fetchall()

        # Process data and generate report
        report_data = {}
        for row in rows:
            student_id, date, status = row
            if student_id not in report_data:
                report_data[student_id] = {'date': date, 'status': status}

        return report_data


class Instructor:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Instructor page")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root, width=454, height=20)
        info_frame.pack(side="top")

        button_frame = Frame(self.root)
        button_frame.pack(side="top")

        # display title
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Instructor Page", fg="#993333",
                           anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # instructor details
        btn_mark_attendance = Button(bottom, text="Mark Student Attendance",
                                     font=('Arial', 14), bg='#993333', height=1, width=40, fg='white',
                                     anchor="center", command=self.mark_attendance)
        btn_mark_attendance.grid(row=3, column=0, padx=10, pady=10)

        btn_view_courses = Button(bottom, text="View Courses",
                                  font=('Arial', 14), bg='#993333', height=1, width=40, fg='white',
                                  anchor="center", command=self.view_courses)
        btn_view_courses.grid(row=4, column=0, padx=10, pady=10)

        btn_view_report = Button(bottom, text="View Attendance Report",
                                 font=('Arial', 14), bg='#993333', height=1, width=40, fg='white',
                                 anchor="center", command=self.view_attendance_report)
        btn_view_report.grid(row=5, column=0, padx=10, pady=10)

        # create home button
        self.home_button = Button(bottom, text="Home", font=('Bookman Old Style', 15), bg="#993333",
                                  height=1, width=20, fg="white", anchor="center", command=self.root.destroy)
        self.home_button.grid(row=6, column=0, padx=10, pady=(10, 20))

        # Initialize the AttendanceStatus class
        self.attendance_status = AttendanceStatus()

    def mark_attendance(self):
        username = simpledialog.askstring("Mark Attendance", "Enter Student Name:")
        status = simpledialog.askstring("Mark Attendance", "Enter Attendance Status (Present/Absent/Late):")
        date = simpledialog.askstring("Mark Attendance", "Enter Date (YYYY-MM-DD):")

        # Call the mark_attendance method from AttendanceStatus class
        self.attendance_status.mark_attendance(username, status, date)

    def view_courses(self):
        # You need to implement the logic to retrieve and display courses
        # For now, let's display a placeholder message
        messagebox.showinfo("View Courses", "Courses: Math, Science, English")

    def view_attendance_report(self):
        # Call the view_attendance_report method from AttendanceStatus class
        report = self.attendance_status.view_attendance_report()

        # Display the report in a new window
        report_window = Toplevel(self.root)
        report_window.title("Attendance Report")

        report_label = Label(report_window, text="Attendance Report", font=('Arial', 16, 'bold'))
        report_label.pack()

        for row in report:
            row_label = Label(report_window, text=row)
            row_label.pack()


def instructor_ui():
    root = Tk()
    application = Instructor(root)
    root.mainloop()


if __name__ == '__main__':
    instructor_ui()

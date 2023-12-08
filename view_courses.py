# view_courses.py

from tkinter import *


class ViewCourses:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("View Courses")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display title
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="View Courses", fg="#993333",
                           anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)


def view_courses_ui():
    root = Tk()
    application = ViewCourses(root)
    root.mainloop()

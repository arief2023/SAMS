from tkinter import *
import main


class About:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("About the program")
        self.root.iconbitmap("hms.ico")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        self.top = Frame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.info_frame = Frame(self.root)
        self.info_frame.pack(side="top")

        # title
        self.About = Label(self.top, font=('Bookman Old Style', 40, 'bold'), text="About Student Attendance System", fg='#993333',
                           anchor='center')
        self.About.grid(row=0, column=0, columnspan=2)

        # Description
        self.desc1 = Label(self.top, font=('Bookman Old Style', 20),
                           text='This is a software that keeps track of student attendance, 24/7.', fg='#993333',
                           anchor='w')
        self.desc2 = Label(self.top, font=("Bookman Old Style", 20),
                           text='With SQLite integration, all your information is stored in a ', fg='#993333',
                           anchor='w')
        self.desc3 = Label(self.top, font=("Bookman Old Style", 20),
                           text='SQLite database file (.db), so student attendance information is not lost when you close the program.',
                           fg='#993333', anchor='w')
        self.desc4 = Label(self.top, font=("Bookman Old Style", 20),
                           text='Seamlessly keep track of Administrator and Instructors of your school.', fg='#993333',
                           anchor='w')
        self.desc5 = Label(self.top, font=("Bookman Old Style", 20),
                           text='View all your Students, Administrator and Instructors , with their information.',
                           fg='#993333', anchor='w')
        self.desc6 = Label(self.top, font=("Bookman Old Style", 20),
                           text='Light, fast and resourceful. The perfect management of school attendance system.',
                           fg='#993333', anchor='w')

        # back to home page
        self.back_home_button = Button(self.bottom, text="Home", font=('Bookman Old Style', 15), bg="#993333",
                                       relief=RIDGE, height=1, width=15, fg="white", anchor="center",
                                       command=self.root.destroy)
        self.back_home_button.grid(row=5, column=2, padx=10, pady=10)

        self.desc1.grid(row=1, column=0, columnspan=2, pady=10)
        self.desc2.grid(row=2, column=0, columnspan=2)
        self.desc3.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        self.desc4.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        self.desc5.grid(row=5, column=0, columnspan=2, pady=(0, 10))
        self.desc6.grid(row=6, column=0, columnspan=2, pady=(0, 10))


def about_ui():
    root = Tk()
    application = About(root)
    root.mainloop()

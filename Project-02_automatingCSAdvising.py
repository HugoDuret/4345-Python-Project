# Hugo DURET
# ID: 20555806
# run on python3

from tkinter import Tk, Label, Button, Entry, Text, OptionMenu, StringVar, Frame, Canvas, Scrollbar, ttk
from PIL import ImageTk, Image

UTRGV_LOGO_PATH = "/home/behemoth/Desktop/4345-Computer Networking/HOMEWORKS/Project2/vaqueros.png"

class main_gui:
    def __init__(self, master):
        self.master = master
        master.title("CS Advising Session")
        master.geometry("800x700")
        master.configure(background='white')
        # In th main window, we create a nested canvas and a nested frame
        # so we can add a scrollbar
        self.canvas = Canvas(master, width=800, height=700, bg='white')
        self.canvas.grid(row=0, column=0, sticky="nsew")
        global_frame = Frame(self.canvas, width=800, height=700, bg='white', padx = 20, pady = 20)
        self.canvas.create_window(0, 0, window=global_frame, anchor='nw')
        scroll = Scrollbar(global_frame)
        scroll.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=scroll.set)
        # The empty row is just here for a design purpose, by adding a horizontal space between
        # the scroll bar and all the elements of the window
        empty_row = Label(global_frame, text="", width = 1, bg = 'white')
        empty_row.grid(row=0, column=5, rowspan = 40, sticky="ns")
        scroll.grid(row=0, column=6, rowspan = 40, sticky="ns")
        global_frame.bind("<Configure>", self.update_scrollregion)

        # TITLE
        self.title_line = Label(global_frame, text="UTRGV B.S. Computer Science\nClass Planning Worksheet", font='Helvetica 14 bold', bg='white')
        self.title_line.grid(row = 0, column = 1, columnspan = 3)

        # UTRGV LOGO
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = Image.open(UTRGV_LOGO_PATH).resize((200,100))
        img_tk = ImageTk.PhotoImage(img)
        # #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.logo = Label(global_frame, image=img_tk, bg='white')
        self.logo.image = img_tk
        self.logo.grid(row = 0, column = 0)

        # NAME
        self.name_label = Label(global_frame, text="Name", font='Helvetica 12', bg='white', pady=10, anchor='e')
        self.name_label.grid(row = 3, column = 0, sticky='NSEW')
        self.name_entry = Entry(global_frame)
        self.name_entry.grid(row = 3, column = 1, sticky='NSEW')

        # ID#
        self.id_label = Label(global_frame, text="ID#", font='Helvetica 12', bg='white', pady=10, padx= 10, anchor='e')
        self.id_label.grid(row = 3, column = 2, sticky='NSEW')
        self.id_entry = Entry(global_frame)
        self.id_entry.grid(row = 3, column = 3, sticky='NSEW')

        # FACULTY ADVISOR
        self.faculty_advisor_label = Label(global_frame, text="FACULTY ADVISOR", font='Helvetica 12', bg='white', pady=10, anchor='e')
        self.faculty_advisor_label.grid(row = 4, column = 0, sticky='NSEW')
        FACULTY_ADVISORS = [
            "Name of advisor 1",
            "Name of advisor 2",
            "Name of advisor 3"
        ]
        self.faculty_advisor_option_menu = ttk.Combobox(global_frame)
        self.faculty_advisor_option_menu['values'] = FACULTY_ADVISORS
        self.faculty_advisor_option_menu.grid(row = 4, column = 1, sticky='NSEW')

        # DATE
        self.date_label = Label(global_frame, text="Date (YYYY-MM-DD)", font='Helvetica 12', bg='white', pady=10, padx= 10, anchor='e')
        self.date_label.grid(row = 4, column = 2, sticky='NSEW')
        # thedate = datetime.datetime.strptime(self.date_entry, '%Y-%m-%d') 
        self.date_entry = Entry(global_frame)
        self.date_entry.grid(row = 4, column = 3, sticky='NSEW')

        # Available terms
        SEMESTERS = [
                "CURRENTLY TAKING",
                "Fall 2020",
                "Summer 2020",
                "Spring 2020",
                "Fall 2019",
                "Spring 2019",
                "Summer 2019"
        ]
        # LIST OF 3 TERMS WITH COURSES CHOICE:
        # for each of the three terms we create a table with entries
        for k in range(3):
            frame = Frame(global_frame, bg = 'white', pady = 30)
            semester_value = StringVar(frame)
            semester_value.set(SEMESTERS[0]) # default value
            semester_option_menu = OptionMenu(frame, semester_value, *SEMESTERS)
            semester_option_menu.config(bg = 'black', fg = 'white')
            semester_option_menu.grid(row = 0, column = 0, columnspan = 3, sticky='NSEW')

            course_number_label = Label(frame, text="Course number", font='Helvetica 12', bg='white', pady=10, highlightcolor='black', highlightbackground='black', highlightthickness=1)
            course_number_label.grid(row = 1, column = 0, sticky='NSEW')
            course_name_label = Label(frame, text="Course name", font='Helvetica 12', bg='white', pady=10, highlightcolor='black', highlightbackground='black', highlightthickness=1)
            course_name_label.grid(row = 1, column = 1, sticky='NSEW')
            credit_hours_label = Label(frame, text="Credit hours", font='Helvetica 12', bg='white', pady=10, highlightcolor='black', highlightbackground='black', highlightthickness=1)
            credit_hours_label.grid(row = 1, column = 2, sticky='NSEW')

            rows = []
            for i in range(7):
                cols = []
                for j in range(3):
                    e = Entry(frame, highlightcolor='black', highlightbackground='black', highlightthickness=1)
                    e.grid(row=i+3, column=j, sticky='NSEW')
                    cols.append(e)
                rows.append(cols)
            
            frame.grid(row = 5 + k, columnspan = 4)

        # NOTES
        self.notes_label = Label(global_frame, text="Notes", font='Helvetica 12 bold', bg='white', pady=10, anchor = 'w')
        self.notes_label.grid(row = 6+3, column = 0, columnspan = 4, sticky='NSEW')
        self.notes_text = Text(global_frame, height = 10)
        self.notes_text.grid(row = 7+3, column = 0, columnspan = 4, sticky='EW')

        # ERROR LABEL SHOWN ONLY WHEN AN ERROR IS TRIGGERED AFTER CLICKING SUBMIT 
        self.error_label = Label(global_frame, text="", font='Helvetica 12 bold', bg='white', fg = 'red', pady=10, anchor = 'w')
        self.error_label.grid(row = 8+3, column = 3, sticky='NSEW')

        # SUBMIT BUTTON 
        self.submit_button = Button(global_frame, text="Submit", command=self.submit)
        self.submit_button.config(bg = 'white')
        self.submit_button.grid(row = 9+3, column = 3, sticky='NSEW')


    def update_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    
    def error_in_entries(self):
        

    def submit(self):
        if not error_in_entries():
            # continue create file


root = Tk()
my_gui = main_gui(root)
root.mainloop()
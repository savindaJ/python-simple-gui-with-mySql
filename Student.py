import email.contentmanager
import string
from tkinter import *


class Person:
    def __int__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def loginBtn(self):
        print('log in')

    def logIn(self):
        windows = Tk()
        windows.title('registration form !')
        windows.geometry('400x200+200+10')
        windows.resizable(0, 0)

        frame = Frame(windows, width='400', height='250', bg='#669999', bd=8)
        frame.place(x=0, y=0)

        status = Label(frame, text='LOG IN !', fg='black', bg='#669999', font=('Calibre', 16, 'bold'))
        status.place(x=170, y=7)

        email = Label(frame, text='e-mail :', fg='#ffffff', bg='#669999', font=('Calibre', 12, 'bold'))
        email.place(x=8, y=50)

        first_name_txt = Entry(windows, width=40, borderwidth=2)
        first_name_txt.place(x=130, y=60)

        pasw = Label(frame, text='Password  :', fg='#ffffff', bg='#669999', font=('Calibre', 12, 'bold'))
        pasw.place(x=8, y=100)

        first_name_txt = Entry(windows, width=40, borderwidth=2)
        first_name_txt.place(x=130, y=110)

        save_butt0n = Button(windows, text='Save', width=4, borderwidth=5, height=1, bg='#ff80ff', fg='blue',
                             cursor='hand2',
                             border=2, font=('#ff3300', 16, 'bold'), command=self.loginBtn)
        save_butt0n.place(x=310, y=150)

        windows.mainloop()


class Student(Person):
    def __int__(self, name, age):
        self.name = name
        self.age = age

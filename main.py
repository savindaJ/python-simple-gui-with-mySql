from tkinter import *
from tkinter import messagebox
import pymysql

from Student import Student

windows = Tk()
windows.title('registration form !')
windows.geometry('540x640+200+10')
windows.resizable(0, 0)


def alertError():
    messagebox.showerror('Error !', 'text Entry is empty please insert values and press SAVE !')


def alertInfo():
    messagebox.showinfo('Success !', 'registration successfully , you will again now !')


def submit():
    if password_txt.get() == '' and username_txt.get() == '':
        alertError()
    else:
        db = pymysql.connect(host='local', user='root', password='80221474', database='sampleRegistration')
        cur = db.cursor()

        cur.execute('use sampleRegistration')

        query = 'insert into user(firstname, lastname, gmail, gender, country, username, password)' \
                'values(%s,%s,%s,%s,%s,%s,%s)'

        cur.execute(query, (
        first_name_txt.get(), last_name_txt.get(), email_txt.get(), gender.getvar(), OM.get(), username_txt.get(),
        password_txt.get()))
        db.commit()
        db.close()
        alertInfo()


def backBtn():
    messagebox.showwarning('warning !', 'this option is not developed !')


def show_password():
    password_txt.configure(show='#')
    check_1.configure(command=hide_1)


def hide_1():
    password_txt.configure(show='')
    check_1.configure(show_password())


OM = StringVar()
country = ['sri lanka', 'india', 'japan']
OM.set('Select Country')

frame = Frame(windows, width='610', height='640', bg='#4287f5', bd=8)
frame.place(x=0, y=0)

start_label = Label(frame, text='Registration Form !', fg='#ffffff', bg='#4287f5', font=('Calibre', 20, 'bold'))
start_label.place(x=130, y=3)

first_name = Label(frame, text='First_name :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
first_name.place(x=8, y=60)

first_name_txt = Entry(windows, width=40, borderwidth=2)
first_name_txt.place(x=200, y=70)

last_name = Label(frame, text='Last_name :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
last_name.place(x=8, y=100)

last_name_txt = Entry(windows, width=40, borderwidth=2)
last_name_txt.place(x=200, y=110)

email = Label(frame, text='e-mail :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
email.place(x=8, y=140)

email_txt = Entry(windows, width=40, borderwidth=2)
email_txt.place(x=200, y=150)

gender = Label(frame, text='Gender :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
gender.place(x=8, y=180)

gender_radioButton = Radiobutton(windows, text='Male', variable=gender, value='Male', font='Tahoma 13 bold')
gender_radioButton.place(x=200, y=180)

gender2_radioButton = Radiobutton(windows, text='Female', variable=gender, value='Female', font='Tahoma 13 bold')
gender2_radioButton.place(x=350, y=180)

countryP = Label(frame, text='country :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
countryP.place(x=8, y=220)

country_dropdown = OptionMenu(windows, OM, *country)
country_dropdown.place(x=200, y=230)
country_dropdown.config(width=18, font=('Calibre', 13, 'bold'))

username = Label(frame, text='User_name :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
username.place(x=8, y=270)

username_txt = Entry(windows, width=40, borderwidth=2)
username_txt.place(x=200, y=280)

password = Label(frame, text='Password :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
password.place(x=8, y=300)

password_txt = Entry(windows, width=40, borderwidth=2)
password_txt.place(x=200, y=310)

confirm_password = Label(frame, text='confirm_password :', fg='#ffffff', bg='#4287f5', font=('Calibre', 12, 'bold'))
confirm_password.place(x=8, y=330)

confirm_password_txt = Entry(windows, width=40, borderwidth=2)
confirm_password_txt.place(x=200, y=340)

save_butt0n = Button(windows, text='Save', width=11, borderwidth=5, height=1, bg='#4287f5', fg='blue', cursor='hand2',
                     border=2, font=('#ff3300', 16, 'bold'), command=submit)
save_butt0n.place(x=210, y=500)

# check button
check_1 = Checkbutton(windows, text='show', bg='white', command=hide_1)
check_1.place(x=450, y=340)

check_2 = Checkbutton(windows, text='show', bg='white')
check_2.place(x=450, y=310)

back_button = Button(windows, text='back <-', width=6, borderwidth=5, height=1, bg='#66ff99', fg='blue', cursor='hand2',
                     border=2, font=('#ff3300', 8, 'bold'), command=backBtn)
back_button.place(x=30, y=600)

windows.mainloop()

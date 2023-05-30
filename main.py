from tkinter import *
from tkinter import messagebox

from Student import Student

windows = Tk()
windows.title('registration form !')
windows.geometry('540x640+200+10')
windows.resizable(0, 0)


def alert():
    messagebox.showinfo('Confirmation', '                                   saved !                            ')
    # alert_view = Tk()
    # alert_view.title('confirm Alert !')
    # alert_view.geometry('300x100+200+10')
    # alert_view.resizable(0, 0)


def printAll():
    student = Student()
    student.name = 'kamal'
    print(student.name)
    alert()


def show_password():
    password_txt.configure(show='#')
    check_1.configure(command=hide_1)


def hide_1():
    password_txt.configure(show='')
    check_1.configure(show_password())


OM = StringVar()
country = ['srilanka', 'india', 'japan', 'koria']
OM.set('Select Country')

frame = Frame(windows, width='610', height='640', bg='#0000b3', bd=8)
frame.place(x=0, y=0)

start_label = Label(frame, text='Registration Form !', fg='#ffffff', bg='#0000b3', font=('Calibre', 20, 'bold'))
start_label.place(x=130, y=3)

first_name = Label(frame, text='First_name :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
first_name.place(x=8, y=60)

first_name_txt = Entry(windows, width=40, borderwidth=2)
first_name_txt.place(x=200, y=70)

last_name = Label(frame, text='Last_name :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
last_name.place(x=8, y=100)

last_name_txt = Entry(windows, width=40, borderwidth=2)
last_name_txt.place(x=200, y=110)

email = Label(frame, text='e-mail :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
email.place(x=8, y=140)

email_txt = Entry(windows, width=40, borderwidth=2)
email_txt.place(x=200, y=150)

gender = Label(frame, text='Gender :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
gender.place(x=8, y=180)

gender_radioButton = Radiobutton(windows, text='Male', variable=gender, value='Male', font='Tahoma 13 bold')
gender_radioButton.place(x=200, y=180)

gender2_radioButton = Radiobutton(windows, text='Female', variable=gender, value='Female', font='Tahoma 13 bold')
gender2_radioButton.place(x=350, y=180)

countryP = Label(frame, text='country :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
countryP.place(x=8, y=220)

country_dropdown = OptionMenu(windows, OM, *country)
country_dropdown.place(x=200, y=230)
country_dropdown.config(width=18, font=('Calibre', 13, 'bold'))

username = Label(frame, text='User_name :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
username.place(x=8, y=270)

username_txt = Entry(windows, width=40, borderwidth=2)
username_txt.place(x=200, y=280)

password = Label(frame, text='Password :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
password.place(x=8, y=300)

password_txt = Entry(windows, width=40, borderwidth=2)
password_txt.place(x=200, y=310)

confirm_password = Label(frame, text='confirm_password :', fg='#ffffff', bg='#0000b3', font=('Calibre', 12, 'bold'))
confirm_password.place(x=8, y=330)

confirm_password_txt = Entry(windows, width=40, borderwidth=2)
confirm_password_txt.place(x=200, y=340)

save_butt0n = Button(windows, text='Save', width=11, borderwidth=5, height=1, bg='#66ff99', fg='blue', cursor='hand2',
                     border=2, font=('#ff3300', 16, 'bold'), command=printAll)
save_butt0n.place(x=210, y=500)

# check button
check_1 = Checkbutton(windows, text='show', bg='white', command=hide_1)
check_1.place(x=450, y=340)

check_2 = Checkbutton(windows, text='show', bg='white')
check_2.place(x=450, y=310)

back_button = Button(windows, text='back <-', width=6, borderwidth=5, height=1, bg='#66ff99', fg='blue', cursor='hand2',
                     border=2, font=('#ff3300', 8, 'bold'),command=printAll)
back_button.place(x=30, y=600)

windows.mainloop()

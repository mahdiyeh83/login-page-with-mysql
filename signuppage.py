from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# Function part


def clear():
    usernameEntry.delete(0, END)
    emailEntry.delete(0, END)
    passwordEntry.delete(0, END)
    repasswordEntry.delete(0, END)
    check.set(0)


def connect_db():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or repasswordEntry.get() == '':
        messagebox.showerror('اخطار', 'لطفا تمامی فیلد هارا پرکنید')
    elif passwordEntry.get() != repasswordEntry.get():
        messagebox.showerror('اخطار', 'رمز عبور مطابقت ندارد')
    elif check.get() == 0:
        messagebox.showerror('اخطار', 'لطفا قوانین وشرایط موافقت کنید')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1111')
            mycursor = con.cursor()
            query = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'userdata'"
            mycursor.execute(query)
            result = mycursor.fetchall()

            if not result:
                query = 'create database userdata'
                mycursor.execute(query)
                query = 'use userdata'
                mycursor.execute(query)
                query = 'create table data(id  int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
                mycursor.execute(query)

        except:
            messagebox.showerror(
                'اخطار', 'خطا در دیتابیس ،لطفا بعدا امتحان کنید')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('اخطار', 'حساب کاربری وجود دارد')
        else:
            query = 'insert into data(username,email,password) values(%s,%s,%s)'
            mycursor.execute(query, (usernameEntry.get(),emailEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('ثبت', 'ثبت نام با موفقیت انجام شد')
            clear()
            signup_window.destroy()
            import signinpage

       


def login_page():
    signup_window.destroy()
    import signinpage


def hide():
    openeye.config(file='./image/eyeclose.png')
    passwordEntry.config(show='•')
    eyeButton.config(command=show)


def show():
    openeye.config(file='./image/eyeopen.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def email_enter(event):
    if emailEntry.get() == 'ایمیل':
        emailEntry.delete(0, END)


def user_enter(event):
    if usernameEntry.get() == 'نام کاربری':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'رمز عبور':
        passwordEntry.delete(0, END)


def repassword_enter(event):
    if repasswordEntry.get() == 'تکرار رمز عبور':
        repasswordEntry.delete(0, END)


# GUI Part
signup_window = Tk()
signup_window.resizable(False, 0)
signup_window.title('ساخت حساب')

bgImage = ImageTk.PhotoImage(file='./image/head1.jpg')
bgLabel = Label(signup_window, image=bgImage)
bgLabel.pack()

heading = Label(signup_window, text='ساخت حساب', font=(
    'IRANSANSWEB', 25, 'bold'), bg='white', fg='#1C6758')
heading.place(x=405, y=200)

# inputs
usernameEntry = Entry(signup_window, width=30, font=(
    'IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
usernameEntry.place(x=340, y=310)
usernameEntry.insert(0, 'نام کاربری')
usernameEntry.bind('<FocusIn>', user_enter)
Frame(signup_window, width=350, height=2, bg='#1C6758').place(x=320, y=340)

emailEntry = Entry(signup_window, width=30, font=(
    'IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
emailEntry.place(x=340, y=380)
emailEntry.insert(0, 'ایمیل')
emailEntry.bind('<FocusIn>', email_enter)
Frame(signup_window, width=350, height=2, bg='#1C6758').place(x=320, y=410)

passwordEntry = Entry(signup_window, width=30, font=(
    'IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
passwordEntry.place(x=340, y=450)
passwordEntry.insert(0, 'رمز عبور')
passwordEntry.bind('<FocusIn>', password_enter)
Frame(signup_window, width=350, height=2, bg='#1C6758').place(x=320, y=480)
openeye = PhotoImage(file='./image/eyeopen.png')
eyeButton = Button(signup_window, image=openeye, bd=0, bg='white',
                   activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=630, y=450)

repasswordEntry = Entry(signup_window, width=30, font=(
    'IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
repasswordEntry.place(x=340, y=520)
repasswordEntry.insert(0, 'تکرار رمز عبور')
repasswordEntry.bind('<FocusIn>', repassword_enter)
Frame(signup_window, width=350, height=2, bg='#1C6758').place(x=320, y=550)

check = IntVar()
termsandcondition = Checkbutton(signup_window, text='با شرایط و قوانین موافقت  میکنم',
                                font=('IRANSANSWEB', '11'), bd=0, fg='#1C6758', bg='white',
                                activebackground='white', activeforeground='#1C6758',
                                cursor='hand2', variable=check)
termsandcondition.place(x=340, y=565)

signupButton = Button(signup_window, text='ساخت حساب', font=('IRANSANSWEB', 15, 'bold'), fg='white', bg='#1C6758',
                      activeforeground='white', activebackground='#1C6758', cursor='hand2', bd=0, width=29, command=connect_db)
signupButton.place(x=320, y=610)


loginButton = Button(signup_window, text='آیا حسابی دارید؟', bd=0, bg='white', activebackground='white',
                     cursor='hand2', font=('IRANSANSWEB', 10, 'bold'), fg='#1C6758', activeforeground='#1C6758')
loginButton.place(x=550, y=680)

gotoButton = Button(signup_window, text='به حساب خود وارد شوید ', font=('IRANSANSWEB', 10, 'bold'), fg='#CD5C08', bg='white',
                    activeforeground='#CD5C08', activebackground='white', cursor='hand2', bd=0, command=login_page)
gotoButton.place(x=420, y=680)


signup_window.mainloop()

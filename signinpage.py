from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# Function part


def forget_pass():
    def change_pass():
        if user_entry.get()=='' or new_entry.get()=='' or renew_entry.get()=='':
          messagebox.showerror('اخطار', 'لطفا تمامی فیلد هارا پرکنید',parent=window)
        elif new_entry.get() != renew_entry.get():
          messagebox.showerror('اخطار', 'رمز عبور مطابقت ندارد',parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='1111',database='userdata')
            mycursor = con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row ==None:
              messagebox.showerror('اخطار', 'نام کاربری اشتباه است ',parent=window)
            else:
              query='updata data set password=%s where username=%s'
              mycursor.execute(query,(new_entry.get(),user_entry.get()))
              con.commit()
              con.close()
              messagebox.showinfo('ثبت', 'تغییر با موفقیت انجام شد',parent=window)
              window.destroy()

    window = Toplevel()
    window.title('تغییر رمز عبور')
    bgImage = ImageTk.PhotoImage(file='./image/forget.png')
    bgLabel = Label(window, image=bgImage)
    bgLabel.pack() 

    heading1 = Label(window, text='تغییر رمزعبور', font=(
    'IRANSANSWEB', 25, 'bold'), bg='white', fg='#1C6758')
    heading1.place(x=230, y=140)
    
    userLabel = Label(window,text='نام کاربری',font=('IRANSANSWEB',11, 'bold'), bg='white', fg='#1C6758')
    userLabel.place(x=145, y=225)
    user_entry = Entry(window, width=30, font=('IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
    user_entry.place(x=145, y=260)
    Frame(window, width=320, height=2, bg='#1C6758').place(x=145, y=280)

    newLabel = Label(window,text='رمز عبور جدید',font=('IRANSANSWEB',11, 'bold'), bg='white', fg='#1C6758')
    newLabel.place(x=145, y=315)
    new_entry = Entry(window, width=30, font=('IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
    new_entry.place(x=145, y=350)
    Frame(window, width=320, height=2, bg='#1C6758').place(x=145, y=370)
   
    renewLabel = Label(window,text='تکرار رمز عبور جدید',font=('IRANSANSWEB',11, 'bold'), bg='white', fg='#1C6758')
    renewLabel.place(x=145, y=400)
    renew_entry = Entry(window, width=30, font=('IRANSANSWEB', 11, 'bold'), bd=0, fg='#1C6758')
    renew_entry.place(x=145, y=435)
    Frame(window, width=320, height=2, bg='#1C6758').place(x=145, y=455)
   
    submitButton=Button(window,text='تغییر رمز',font=('IRANSANSWEB',15,'bold'),fg='white',bg='#1C6758',
                   activeforeground='white',activebackground='#1C6758',cursor='hand2',bd=0,width=26,command=change_pass)
    submitButton.place(x=145,y=550)





    window.mainloop()

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
       messagebox.showerror('اخطار', 'لطفا تمامی فیلد هارا پرکنید')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1111')
            mycursor = con.cursor()
        except:
            messagebox.showerror('اخطار', 'خطا در دیتابیس ،لطفا بعدا امتحان کنید')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row ==None:
            messagebox.showerror('اخطار', 'نام کاربری یا رمز عبور اشتباه است ')
        else:
            messagebox.showerror('خوش آمدید', 'به حساب خود خوش برگشتید')
 
def signup_page():
    login_window.destroy()
    import signuppage

def hide():
    openeye.config(file='./image/eyeclose.png')
    passwordEntry.config(show='•')
    eyeButton.config(command=show)

def show():
    openeye.config(file='./image/eyeopen.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='نام کاربری':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='رمز عبور':
        passwordEntry.delete(0,END)

# GUI Part
login_window=Tk()
login_window.resizable(0,0)
login_window.title('ورود')

bgImage=ImageTk.PhotoImage(file='./image/head1.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()

heading=Label(login_window,text='ورود کاربر',font=('IRANSANSWEB',25,'bold'),bg='white',fg='#1C6758')
heading.place(x=438,y=200)

# inputs
usernameEntry=Entry(login_window,width=30,font=('IRANSANSWEB',11,'bold'),bd=0,fg='#1C6758')
usernameEntry.place(x=340,y=310)
usernameEntry.insert(0,'نام کاربری')
usernameEntry.bind('<FocusIn>',user_enter)
Frame(login_window,width=350,height=2,bg='#1C6758').place(x=320,y=340)


passwordEntry=Entry(login_window,width=30,font=('IRANSANSWEB',11,'bold'),bd=0,fg='#1C6758')
passwordEntry.place(x=340,y=380)
passwordEntry.insert(0,'رمز عبور')
passwordEntry.bind('<FocusIn>',password_enter)
Frame(login_window,width=350,height=2,bg='#1C6758').place(x=320,y=410)
openeye=PhotoImage(file='./image/eyeopen.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=620,y=380)

forgetButton=Button(login_window,text='آیا رمز خود را فراموش کرده اید؟',bd=0,bg='white',activebackground='white',cursor='hand2',font=('IRANSANSWEB',10,'bold'),fg='#1C6758',activeforeground='#1C6758',command=forget_pass)
forgetButton.place(x=500,y=430)

# loginbtn
loginButton=Button(login_window,text='ورود',font=('IRANSANSWEB',15,'bold'),fg='white',bg='#1C6758',
                   activeforeground='white',activebackground='#1C6758',cursor='hand2',bd=0,width=29,command=login_user)
loginButton.place(x=320,y=500)




orLabel=Label(login_window,text='------------------------- یا -------------------------',font=('IRANSANSWEB',16),fg='#1C6758',bg='white')
orLabel.place(x=330,y=555)


facebook_logo=PhotoImage(file='./image/icons8-facebook-24.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=430,y=600)

google_logo=PhotoImage(file='./image/icons8-google-24.png')
ggLabel=Label(login_window,image=google_logo,bg='white')
ggLabel.place(x=485,y=600)

phone_logo=PhotoImage(file='./image/icons8-phone-24.png')
pnLabel=Label(login_window,image=phone_logo,bg='white')
pnLabel.place(x=540,y=600)

signupButton=Button(login_window,text='آیا حسابی ندارید؟',bd=0,bg='white',activebackground='white',cursor='hand2',font=('IRANSANSWEB',10,'bold'),fg='#1C6758',activeforeground='#1C6758')
signupButton.place(x=550,y=650)

newaccountButton=Button(login_window,text='حساب خود را بسازید',font=('IRANSANSWEB',10,'bold'),fg='#CD5C08',bg='white',
                   activeforeground='#CD5C08',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=440,y=650)

login_window.mainloop()

import hashlib 
from tkinter import *
from firebase import firebase
from tkinter import messagebox as msgbox

firebase=firebase.FirebaseApplication("https://registration-py-default-rtdb.firebaseio.com/",None)
registration_window = Tk()
registration_window.geometry("400x400")
registration_window.config(bg="orange")

login_username_entry=""
login_password_entry=""

def login(): 
    global login_username_entry
    global login_password_entry
    username=login_username_entry.get()
    password=login_password_entry.get()
    encrypted_password=hashlib.md5(password.encode())
    hexadecimal_password=encrypted_password.hexdigest()
    get_data=firebase.get('/',username)
    print(get_data)
    if(get_data != None):
        if(get_data==hexadecimal_password):
            msgbox.showinfo(title="Report",message="Successfully logged in")
        else:
            msgbox.showinfo(title="Error",message="Please Check Your Password")
    else:
        msgbox.showinfo(title="Error",message="User not registered! \nGet yourself registered first to login")
         
def register(): 
    username=username_entry.get()
    password=password_entry.get()
    space=" "
    if space in username or space in password:
        msgbox.showinfo(title="Error",message="Please Check Your Password and Username for NO spaces")
        
    else:
        hashed_value=hashlib.md5(password.encode())
        hex_value=hashed_value.hexdigest()
        print(hex_value)
        put_data=firebase.put("/",username,hex_value)
        #print(hashlib.md5(password.encode()).hexdigest())
        #put_data=firebase.put("/",username,hashlib.md5(password.encode()).hexdigest())
        msgbox.showinfo(title="Report",message="Registration Done")
    
def login_window():
    global login_username_entry
    global login_password_entry
    
    registration_window.destroy()
    
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.config(bg="lightgreen")
    
    log_heading_label = Label(login_window, text="Log In" , font = ('arial 18 bold'),bg="lightgreen")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = ('arial 13'),bg="lightgreen")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = ('arial 13'),bg="lightgreen")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT,fg="blue",bg="aqua")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = ('arial 18 bold',),bg="orange")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = ('arial 13'),bg="orange")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = ('arial 13'),bg="orange")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10,bg="aqua",fg="blue")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT,bg="blue",fg="aqua")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()
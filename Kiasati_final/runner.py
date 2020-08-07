import sqlite3
from base import win
from tkinter import ttk
from login import opensignin, opensignup

with sqlite3.connect('users.db') as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS 
    users
    (username TEXT NOT NULL PRIMARY KEY,
    password TEXT NOT NULL,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    games INTEGER,
    wins INTEGER,
    isAdmin Boolean
    );""")
cursor.execute("select * from users where username = 'admin' ")
isFirst = cursor.fetchone()
if isFirst is None:
    cursor.execute("INSERT INTO users VALUES('admin','123456','Hamraaz','Kiasati','0','0',true)")
db.commit()
db.close()

btn_login = ttk.Button(win, text='Sign in', command=opensignin)
btn_login.place(relx=0.3, rely=0.3)
btn_signup = ttk.Button(win, text='Sign up', command=opensignup)
btn_signup.place(relx=0.3, rely=0.6)
win.mainloop()

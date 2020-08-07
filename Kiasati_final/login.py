from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import SosGame
from base import win
import random


def opensignin():
    login = Toplevel(win)
    login.title('Sign in')
    login.geometry("400x200")
    login.resizable(False, False)

    entry_username = Entry(login, width=40)
    entry_username.place(relx=0.3, rely=0.05)
    lb_username = Label(login, text='username : ')
    lb_username.place(relx=0.1, rely=0.05)

    entry_password = Entry(login, width=40, show='*')
    entry_password.place(relx=0.3, rely=0.25)
    lb_password = Label(login, text='Password : ')
    lb_password.place(relx=0.1, rely=0.25)

    def signin():
        try:
            connection = sqlite3.connect('users.db')
            c = connection.cursor()

            c.execute("select * from users where username = '%s' and password = '%s'"
                      % (entry_username.get(), entry_password.get()))
            for userinput in c:
                pass
            connection.commit()
            connection.close()

            if userinput[0] == entry_username.get() and userinput[1] == entry_password.get():
                if userinput[0] == 'admin' and userinput[1] == '123456':
                    first = Toplevel(win)
                    first.geometry("400x400")
                    first.resizable(False, False)
                    first.title("choose Your new Password")
                    entry_password_first = Entry(first, width=40, show='*')
                    entry_password_first.place(relx=0.3, rely=0.2)
                    lb_password_first = Label(first, text='password : ')
                    lb_password_first.place(relx=0.1, rely=0.2)

                    entry_rpassword_first = Entry(first, width=40, show='*')
                    entry_rpassword_first.place(relx=0.3, rely=0.3)
                    lb_rpassword_first = Label(first, text='Reenter pass :')
                    lb_rpassword_first.place(relx=0.1, rely=0.30)

                    def first_time_login():
                        if entry_password_first.get() == entry_rpassword_first.get() and entry_password.get() != entry_rpassword_first.get():
                            connection_first = sqlite3.connect('users.db')
                            c_first = connection_first.cursor()
                            update_point = """UPDATE users
                                                SET password = ?
                                                WHERE
                                                username = 'admin'"""
                            c_first.execute(update_point, [entry_password_first.get()])
                            connection_first.commit()
                            connection_first.close()
                            first.destroy()
                            messagebox.showinfo("Success", "Done!")
                        else:
                            messagebox.showerror("ERROR", "Reenter password is mistake")
                            entry_password_first.delete(0, END)
                            entry_rpassword_first.delete(0, END)

                    btn_signup = ttk.Button(first, text='Confirm', command=first_time_login)
                    btn_signup.place(relx=0.5, rely=0.75)
                login_username = userinput[0]
                login_first = userinput[2]
                login_last = userinput[3]
                login_games = userinput[4]
                login_wins = userinput[5]
                login_isAdmin = userinput[6]
                Users = []

                def delete_user():
                    with sqlite3.connect('users.db') as db:
                        cursor = db.cursor()
                    delete_user = "DELETE FROM users WHERE username = ?"
                    cursor.execute(delete_user, [login_username])
                    db.commit()
                    find_user = "SELECT * FROM users WHERE username = ?"
                    cursor.execute(find_user, [login_username])
                    results = cursor.fetchone()
                    if results is None:
                        messagebox.showinfo('Success', "Delete Complete")
                        db.close()
                        profile.destroy()

                def show_users_again():
                    show_users()

                def show_users():
                    def select_user():
                        for j in range(len(Users)):
                            if Users[j][0] == my_listbox.get(ANCHOR):
                                selected_user = Users[j][0]
                                selected_first = Users[j][2]
                                selected_last = Users[j][3]
                                selected_games = Users[j][4]
                                selected_wins = Users[j][5]

                        def edit_selected_user():
                            selected_profile.withdraw()
                            edit_selected = Toplevel(selected_profile)
                            edit_selected.title('edit page')
                            edit_selected.geometry("400x400")
                            edit_selected.resizable(False, False)

                            selected_entry_first = Entry(edit_selected, width=40)
                            selected_entry_first.place(relx=0.3, rely=0.1)
                            selected_lb_first_name = Label(edit_selected, text='First name :')
                            selected_lb_first_name.place(relx=0.1, rely=0.1)

                            selected_entry_last = Entry(edit_selected, width=40)
                            selected_entry_last.place(relx=0.3, rely=0.2)
                            selected_lb_first_name = Label(edit_selected, text='LastName :')
                            selected_lb_first_name.place(relx=0.1, rely=0.2)

                            def selected_again():
                                edit_selected.destroy()
                                select_user()

                            def selected_updatedb():
                                try:
                                    selected_connection = sqlite3.connect('users.db')
                                    selected_c = selected_connection.cursor()
                                    print('0')
                                    update_user = """UPDATE users
                                                    SET first = ?,
                                                        last = ?
                                                 WHERE
                                                    username = ?"""
                                    print(selected_entry_first.get())
                                    print(selected_entry_last.get())
                                    print(selected_user)
                                    selected_c.execute(update_user,
                                                       [selected_entry_first.get(), selected_entry_last.get(),
                                                        selected_user])
                                    print('0')

                                    selected_connection.commit()
                                    selected_connection.close()
                                    edit_selected.destroy()
                                    show_page.destroy()
                                    show_users()
                                    messagebox.showinfo("Success", "Done!")
                                except:
                                    messagebox.showerror('Oops!!', "try Again")

                            selected_btn_confirm = ttk.Button(edit_selected, text='Confirm', command=selected_updatedb)
                            selected_btn_confirm.place(relx=0.2, rely=0.75)

                            selected_btn_exit = ttk.Button(edit_selected, text='Cancel', command=selected_again)
                            selected_btn_exit.place(relx=0.6, rely=0.75)

                        def delete_selected_user():
                            with sqlite3.connect('users.db') as in_db:
                                in_cursor = in_db.cursor()
                            delete_select_user = "DELETE FROM users WHERE username = ?"
                            print(selected_user)
                            in_cursor.execute(delete_select_user, [selected_user])
                            in_db.commit()
                            find_selected_user = "SELECT * FROM users WHERE username = ?"
                            in_cursor.execute(find_selected_user, [selected_user])
                            selected_results = in_cursor.fetchone()

                            if selected_results is None:
                                messagebox.showinfo('Success', "Delete Complete")
                                db.close()
                                selected_profile.destroy()
                                show_page.destroy()
                                show_users_again()

                        selected_profile = Toplevel(login)
                        selected_profile.title('Hi')
                        selected_profile.geometry("400x400")
                        selected_profile.resizable(False, False)
                        selected_first = Label(selected_profile, width=40, text=selected_first)
                        selected_first.place(relx=0.3, rely=0.1)
                        selected_first = Label(selected_profile, text='First name :')
                        selected_first.place(relx=0.1, rely=0.1)

                        selected_last = Label(selected_profile, width=40, text=selected_last)
                        selected_last.place(relx=0.3, rely=0.2)
                        selected_last = Label(selected_profile, text='LastName :')
                        selected_last.place(relx=0.1, rely=0.2)

                        selected_UserName = Label(selected_profile, width=40, text=selected_user)
                        selected_UserName.place(relx=0.3, rely=0.3)
                        selected_UserName = Label(selected_profile, text='UserName :')
                        selected_UserName.place(relx=0.1, rely=0.3)

                        selected_Games = Label(selected_profile, width=40, text=selected_games)
                        selected_Games.place(relx=0.3, rely=0.4)
                        selected_Games = Label(selected_profile, text='Games :')
                        selected_Games.place(relx=0.1, rely=0.4)

                        selected_Wins = Label(selected_profile, width=40, text=selected_wins)
                        selected_Wins.place(relx=0.3, rely=0.5)
                        selected_Wins = Label(selected_profile, text='Wins :')
                        selected_Wins.place(relx=0.1, rely=0.5)
                        btn_edit_user = ttk.Button(selected_profile, text='Edit', command=edit_selected_user)
                        btn_edit_user.place(relx=0.2, rely=0.75)

                        btn_delete_user = ttk.Button(selected_profile, text='Delete', command=delete_selected_user)
                        btn_delete_user.place(relx=0.4, rely=0.75)

                        btn_exit_list = ttk.Button(selected_profile, text='Back', command=selected_profile.destroy)
                        btn_exit_list.place(relx=0.6, rely=0.75)

                    show_page = Toplevel(profile)
                    show_page.title('Users')
                    show_page.geometry("400x400")
                    show_page.resizable(False, False)
                    my_listbox = Listbox(show_page)
                    with sqlite3.connect('users.db') as db:
                        cursor = db.cursor()
                    find_user = "SELECT * FROM users"
                    cursor.execute(find_user)
                    results = cursor.fetchall()
                    if results:
                        for i in range(1, len(results)):
                            Users.append([results[i][0], results[i][1], results[i][2], results[i][3], results[i][4],
                                          results[i][5]])
                            my_listbox.insert(END, results[i][0])
                    my_listbox.pack()
                    btn_confirm = ttk.Button(show_page, text='Show', command=select_user)
                    btn_confirm.place(relx=0.2, rely=0.75)

                    btn_exit = ttk.Button(show_page, text='Back', command=show_page.destroy)
                    btn_exit.place(relx=0.6, rely=0.75)

                def edit_page():
                    profile.withdraw()
                    edit = Toplevel(profile)
                    edit.title('edit page')
                    edit.geometry("400x400")
                    edit.resizable(False, False)

                    entry_password = Entry(edit, width=40, show='*')
                    entry_password.place(relx=0.3, rely=0.2)
                    lb_password = Label(edit, text='password : ')
                    lb_password.place(relx=0.1, rely=0.2)

                    entry_rpassword = Entry(edit, width=40, show='*')
                    entry_rpassword.place(relx=0.3, rely=0.3)
                    lb_rpassword = Label(edit, text='Reenter pass :')
                    lb_rpassword.place(relx=0.1, rely=0.30)

                    entry_first = Entry(edit, width=40)
                    entry_first.place(relx=0.3, rely=0.4)
                    lb_first_name = Label(edit, text='First name :')
                    lb_first_name.place(relx=0.1, rely=0.4)

                    entry_last = Entry(edit, width=40)
                    entry_last.place(relx=0.3, rely=0.5)
                    lb_first_name = Label(edit, text='LastName :')
                    lb_first_name.place(relx=0.1, rely=0.5)

                    def signin_again():
                        edit.destroy()
                        signin()

                    def updatedb():
                        try:

                            if entry_password.get() == entry_rpassword.get():
                                connection = sqlite3.connect('users.db')
                                c = connection.cursor()
                                update_user = """UPDATE users
                                                SET first = ?,
                                                    last = ?,
                                                    password = ?
                                             WHERE
                                                username = ?"""
                                c.execute(update_user,
                                          [entry_first.get(), entry_last.get(), entry_password.get(),
                                           login_username])
                                # c.execute(
                                #     "update users(password,first,last) values('%s','%s','%s') where username= '%s'"
                                #     % (entry_password.get(), entry_first.get(), entry_last.get(),login_username))
                                connection.commit()
                                connection.close()
                                edit.destroy()
                                signin()
                                messagebox.showinfo("Success", "Done!")
                            else:
                                messagebox.showerror("ERROR", "Reenter password is mistake")
                                entry_username.delete(0, END)
                                entry_password.delete(0, END)
                                entry_rpassword.delete(0, END)

                        except:
                            messagebox.showerror("ERROR", "some error was thrown please try again later")
                            entry_username.delete(0, END)
                            entry_password.delete(0, END)
                            entry_rpassword.delete(0, END)

                    btn_confirm = ttk.Button(edit, text='Confirm', command=updatedb)
                    btn_confirm.place(relx=0.2, rely=0.75)

                    btn_exit = ttk.Button(edit, text='Cancel', command=signin_again)
                    btn_exit.place(relx=0.6, rely=0.75)

                def start_game():
                    def start_sos():
                        if int(entry_n.get()) > 2:
                            rand = random.randint(0, 1)
                            if rand:
                                SosGame.start_game_sos(int(entry_n.get()), login_username, my_listbox.get(ANCHOR))
                            else:
                                SosGame.start_game_sos(int(entry_n.get()), my_listbox.get(ANCHOR), login_username)

                        else:
                            messagebox.showerror('Oops!!', "Your rows must be greater than 3")

                    show_page = Toplevel(profile)
                    show_page.title('Users')
                    show_page.geometry("400x400")
                    show_page.resizable(False, False)
                    my_listbox = Listbox(show_page)
                    with sqlite3.connect('users.db') as db:
                        cursor = db.cursor()
                    find_user = "SELECT * FROM users where username !=?"
                    cursor.execute(find_user, [login_username])
                    results = cursor.fetchall()
                    if results:
                        for i in range(0, len(results)):
                            Users.append([results[i][0], results[i][1], results[i][2], results[i][3], results[i][4],
                                          results[i][5]])
                            my_listbox.insert(END, results[i][0])
                    my_listbox.pack()
                    lbl_n = ttk.Label(show_page, text='Rows : ')
                    lbl_n.place(relx=0.2, rely=0.6)
                    entry_n = ttk.Entry(show_page)
                    entry_n.place(relx=0.3, rely=0.6)

                    btn_confirm = ttk.Button(show_page, text='Play', command=start_sos)
                    btn_confirm.place(relx=0.2, rely=0.75)

                    btn_exit = ttk.Button(show_page, text='Back', command=show_page.destroy)
                    btn_exit.place(relx=0.6, rely=0.75)

                login.withdraw()
                profile = Toplevel(login)
                profile.title('Hi')
                profile.geometry("400x400")
                profile.resizable(False, False)
                label_first = Label(profile, width=40, text=login_first)
                label_first.place(relx=0.3, rely=0.1)
                lb_first = Label(profile, text='First name :')
                lb_first.place(relx=0.1, rely=0.1)

                label_last = Label(profile, width=40, text=login_last)
                label_last.place(relx=0.3, rely=0.2)
                lb_last = Label(profile, text='LastName :')
                lb_last.place(relx=0.1, rely=0.2)

                label_UserName = Label(profile, width=40, text=login_username)
                label_UserName.place(relx=0.3, rely=0.3)
                lb_UserName = Label(profile, text='UserName :')
                lb_UserName.place(relx=0.1, rely=0.3)

                label_Games = Label(profile, width=40, text=login_games)
                label_Games.place(relx=0.3, rely=0.4)
                lb_Games = Label(profile, text='Games :')
                lb_Games.place(relx=0.1, rely=0.4)

                label_Wins = Label(profile, width=40, text=login_wins)
                label_Wins.place(relx=0.3, rely=0.5)
                lb_Wins = Label(profile, text='Wins :')
                lb_Wins.place(relx=0.1, rely=0.5)

                btn_edit = ttk.Button(profile, text='Edit', command=edit_page)
                btn_edit.place(relx=0.2, rely=0.75)

                btn_start = ttk.Button(profile, text='Start Game', command=start_game)
                btn_start.place(relx=0.6, rely=0.75)
                if login_isAdmin:
                    btn_show_users = ttk.Button(profile, text='Show Users', command=show_users)
                    btn_show_users.place(relx=0.2, rely=0.9)

                    btn_show_users = ttk.Button(profile, text='Create User', command=opensignup)
                    btn_show_users.place(relx=0.6, rely=0.9)
                else:
                    btn_delete_my = ttk.Button(profile, text='DELETE My Self', command=delete_user)
                    btn_delete_my.place(relx=0.4, rely=0.9)

            else:
                messagebox.showerror("ERROR", "bad username or password")
                entry_username.delete(0, END)
                entry_password.delete(0, END)

        except:
            messagebox.showerror("ERROR", "bad username or password")
            entry_username.delete(0, END)
            entry_password.delete(0, END)

    btn_signin = ttk.Button(login, text='Login', command=signin)
    btn_signin.place(relx=0.5, rely=0.75)


def opensignup():
    signup = Toplevel(win)
    signup.title('Sign up')
    signup.geometry("400x200")
    signup.resizable(False, False)

    entry_username = Entry(signup, width=40)
    entry_username.place(relx=0.3, rely=0.1)
    lb_username = Label(signup, text='username : ')
    lb_username.place(relx=0.1, rely=0.1)

    entry_password = Entry(signup, width=40, show='*')
    entry_password.place(relx=0.3, rely=0.2)
    lb_password = Label(signup, text='password : ')
    lb_password.place(relx=0.1, rely=0.2)

    entry_rpassword = Entry(signup, width=40, show='*')
    entry_rpassword.place(relx=0.3, rely=0.3)
    lb_rpassword = Label(signup, text='Reenter pass :')
    lb_rpassword.place(relx=0.1, rely=0.30)

    entry_first = Entry(signup, width=40)
    entry_first.place(relx=0.3, rely=0.4)
    lb_first = Label(signup, text='First name :')
    lb_first.place(relx=0.1, rely=0.4)

    entry_last = Entry(signup, width=40)
    entry_last.place(relx=0.3, rely=0.5)
    lb_last = Label(signup, text='LastName :')
    lb_last.place(relx=0.1, rely=0.5)

    def connecttodb():
        try:
            if entry_password.get() == entry_rpassword.get():
                connection = sqlite3.connect('users.db')
                c = connection.cursor()
                c.execute(
                    "insert into users(username,password,first,last,games,wins,isAdmin) values('%s','%s','%s','%s',0,0,0)"
                    % (entry_username.get(), entry_password.get(), entry_first.get(), entry_last.get()))
                connection.commit()
                connection.close()
                signup.destroy()
                messagebox.showinfo("Success", "Done!")
            else:
                messagebox.showerror("ERROR", "Reenter password is mistake")
                entry_username.delete(0, END)
                entry_password.delete(0, END)
                entry_rpassword.delete(0, END)

        except:
            messagebox.showerror("ERROR", "this username is already exist!")
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_rpassword.delete(0, END)

    btn_signup = ttk.Button(signup, text='Sign up', command=connecttodb)
    btn_signup.place(relx=0.5, rely=0.75)

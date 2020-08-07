import sqlite3
from tkinter import *
from base import win
from tkinter import messagebox as ms


def start_game_sos(n_games, user1, user2):
    global player_one_point
    global player_two_point
    global player_one_color
    global player_two_color
    global player_flag
    global flag
    global buttons
    global player_two_helps
    global player_one_helps
    player_one_helps = 3
    player_two_helps = 3
    player_one_point = 0
    player_two_point = 0
    player_one_color = 'red'
    player_two_color = 'blue'
    player_flag = True
    flag = player_one_color
    buttons = []
    tk = Toplevel(win)
    tk.title("Sos Game")
    tk.geometry("800x700")
    tk.resizable(False, False)
    n = n_games

    def Help():
        global player_one_point
        global player_two_point
        global player_one_color
        global player_two_color
        global player_flag
        global player_one_helps
        global player_two_helps
        global flag
        global buttons
        if player_flag:
            if player_one_point:
                if player_one_helps:
                    for i in range(n):
                        for j in range(n):
                            if i + 2 < n and j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 2][j + 2][
                                'text'] == 'S' and \
                                    buttons[i + 1][j + 1]['text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 1][j + 1].config(bg='yellow')
                                return
                            if i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 2][j]['text'] == 'S' and \
                                    buttons[i + 1][j][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 1][j].config(bg='yellow')
                                return
                            if j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i][j + 2]['text'] == 'S' and \
                                    buttons[i][j + 1][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i][j + 1].config(bg='yellow')
                                return

                            if i + 2 < n and j - 2 >= 0 and buttons[i][j]['text'] == 'S' and buttons[i + 2][j - 2][
                                'text'] == 'S' and \
                                    buttons[i + 1][j - 1][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 1][j - 1].config(bg='yellow')
                                return

                            if i + 2 < n and j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 1][j + 1][
                                'text'] == 'O' and \
                                    buttons[i + 2][j + 2]['text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 2][j + 2].config(bg='yellow')
                                return
                            if i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 1][j]['text'] == 'O' and \
                                    buttons[i + 2][j][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 2][j].config(bg='yellow')
                                return
                            if j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i][j + 1]['text'] == 'O' and \
                                    buttons[i][j + 2][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i][j + 2].config(bg='yellow')
                                return
                            if i + 2 < n and j + 2 < n and buttons[i + 2][j + 2]['text'] == 'S' and \
                                    buttons[i + 1][j + 1]['text'] == 'O' and \
                                    buttons[i][j]['text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i][j].config(bg='yellow')
                                return
                            if i + 2 < n and buttons[i + 2][j]['text'] == 'S' and buttons[i + 1][j]['text'] == 'O' and \
                                    buttons[i][j][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i][j].config(bg='yellow')
                                return
                            if j + 2 < n and buttons[i][j + 2]['text'] == 'S' and buttons[i][j + 1]['text'] == 'O' and \
                                    buttons[i][j][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i][j].config(bg='yellow')
                                return

                            if j + 2 < n and i - 2 >= 0 and buttons[i][j]['text'] == 'S' and buttons[i - 2][j + 2][
                                'text'] == 'S' and \
                                    buttons[i - 1][j + 1][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i - 1][j + 1].config(bg='yellow')
                                return

                            if j - 2 >= 0 and i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 2][j - 2][
                                'text'] == 'S' and \
                                    buttons[i + 1][j - 1][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 1][j - 1].config(bg='yellow')
                                return

                            if j + 2 < n and i - 2 >= 0 and buttons[i][j]['text'] == 'S' and buttons[i - 1][j + 1][
                                'text'] == 'O' and \
                                    buttons[i - 2][j + 2][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i - 2][j + 2].config(bg='yellow')
                                return

                            if j - 2 >= 0 and i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 1][j - 1][
                                'text'] == 'O' and \
                                    buttons[i + 2][j - 2][
                                        'text'] == '':
                                player_one_point -= 1
                                player_one_helps -= 1
                                lb_player_one_remain_helps['text'] = int(lb_player_one_remain_helps['text']) - 1
                                buttons[i + 2][j - 2].config(bg='yellow')
                                return
                else:
                    ms.showerror('Oops!!', "You don't have enough helps")
            else:
                ms.showerror('Oops!!', "You don't have enough point for help")
        else:
            if player_two_point:
                if player_two_helps:
                    for i in range(0, n):
                        for j in range(0, n):
                            if i + 2 < n and j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 2][j + 2][
                                'text'] == 'S' and \
                                    buttons[i + 1][j + 1]['text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 1][j + 1].config(bg='yellow')
                                return
                            if i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 2][j]['text'] == 'S' and \
                                    buttons[i + 1][j][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 1][j].config(bg='yellow')
                                return
                            if j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i][j + 2]['text'] == 'S' and \
                                    buttons[i][j + 1][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i][j + 1].config(bg='yellow')
                                return

                            if i + 2 < n and j - 2 >= 0 and buttons[i][j]['text'] == 'S' and buttons[i + 2][j - 2][
                                'text'] == 'S' and \
                                    buttons[i + 1][j - 1][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 1][j - 1].config(bg='yellow')
                                return

                            if i + 2 < n and j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 1][j + 1][
                                'text'] == 'O' and \
                                    buttons[i + 2][j + 2]['text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 2][j + 2].config(bg='yellow')
                                return
                            if i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 1][j]['text'] == 'O' and \
                                    buttons[i + 2][j][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 2][j].config(bg='yellow')
                                return
                            if j + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i][j + 1]['text'] == 'O' and \
                                    buttons[i][j + 2][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i][j + 2].config(bg='yellow')
                                return
                            if i + 2 < n and j + 2 < n and buttons[i + 2][j + 2]['text'] == 'S' and \
                                    buttons[i + 1][j + 1]['text'] == 'O' and \
                                    buttons[i][j]['text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i][j].config(bg='yellow')
                                return
                            if i + 2 < n and buttons[i + 2][j]['text'] == 'S' and buttons[i + 1][j]['text'] == 'O' and \
                                    buttons[i][j][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i][j].config(bg='yellow')
                                return
                            if j + 2 < n and buttons[i][j + 2]['text'] == 'S' and buttons[i][j + 1]['text'] == 'O' and \
                                    buttons[i][j][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i][j].config(bg='yellow')
                                return

                            if j + 2 < n and i - 2 >= 0 and buttons[i][j]['text'] == 'S' and buttons[i - 2][j + 2][
                                'text'] == 'S' and \
                                    buttons[i - 1][j + 1][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i - 1][j + 1].config(bg='yellow')
                                return

                            if j - 2 >= 0 and i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 2][j - 2][
                                'text'] == 'S' and \
                                    buttons[i + 1][j - 1][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 1][j - 1].config(bg='yellow')
                                return

                            if j + 2 < n and i - 2 >= 0 and buttons[i][j]['text'] == 'S' and buttons[i - 1][j + 1][
                                'text'] == 'O' and \
                                    buttons[i - 2][j + 2][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i - 2][j + 2].config(bg='yellow')
                                return

                            if j - 2 >= 0 and i + 2 < n and buttons[i][j]['text'] == 'S' and buttons[i + 1][j - 1][
                                'text'] == 'O' and \
                                    buttons[i + 2][j - 2][
                                        'text'] == '':
                                player_two_point -= 1
                                player_two_helps -= 1
                                lb_player_two_remain_helps['text'] = int(lb_player_two_remain_helps['text']) - 1
                                buttons[i + 2][j - 2].config(bg='yellow')
                                return

                else:
                    ms.showerror('Oops!!', "You don't have enough helps")
            else:
                ms.showerror('Oops!!', "You don't have enough point for help")

    first_user = Label(tk, width=40, text=user1)
    first_user.place(relx=0.15, rely=0.1)
    lb_first_user = Label(tk, text='First Player :')
    lb_first_user.place(relx=0.1, rely=0.1)
    first_user_point = Label(tk, width=40, text=player_one_point)
    first_user_point.place(relx=0.15, rely=0.15)
    lb_first_user_point = Label(tk, text='Point :')
    lb_first_user_point.place(relx=0.1, rely=0.15)
    second_user = Label(tk, width=40, text=user2)
    second_user.place(relx=0.65, rely=0.1)
    lb_second_user = Label(tk, text='Second PLayer :')
    lb_second_user.place(relx=0.6, rely=0.1)
    second_user_point = Label(tk, width=40, text=player_two_point)
    second_user_point.place(relx=0.65, rely=0.15)
    lb_second_user_point = Label(tk, text='Point :')
    lb_second_user_point.place(relx=0.6, rely=0.15)
    turn = Label(tk, width=40, text=user1)
    turn.place(relx=0.3, rely=0.05)
    lb_player_one_helps = Label(tk, text='Player one helps :')
    lb_player_one_helps.place(relx=0.1, rely=0.95)
    lb_player_one_remain_helps = Label(tk, text='3')
    lb_player_one_remain_helps.place(relx=0.25, rely=0.95)
    lb_player_two_helps = Label(tk, text='Player two helps :')
    lb_player_two_helps.place(relx=0.6, rely=0.95)
    lb_player_two_remain_helps = Label(tk, text='3')
    lb_player_two_remain_helps.place(relx=0.75, rely=0.95)
    btn_help = Button(tk, text='Help', command=Help)
    btn_help.place(relx=0.5, rely=0.95)

    def update_db_points():
        if player_one_point > player_two_point:
            connection = sqlite3.connect('users.db')
            c = connection.cursor()
            update_point = """UPDATE users
                            SET games = games + 1,
                                wins = wins +1
                            WHERE
                            username = ?"""
            c.execute(update_point, [user1])
            update_point = """UPDATE users
                                    SET games = games + 1
                                    WHERE
                                    username = ?"""
            c.execute(update_point, [user2])
            connection.commit()
            connection.close()
        elif player_two_point > player_one_point:
            connection = sqlite3.connect('users.db')
            c = connection.cursor()
            update_point = """UPDATE users
                            SET games = games + 1,
                                wins = wins +1
                            WHERE
                            username = ?"""
            c.execute(update_point, [user2])
            update_point = """UPDATE users
                                    SET games = games + 1
                                    WHERE
                                    username = ?"""
            c.execute(update_point, [user1])
            connection.commit()
            connection.close()
        else:
            connection = sqlite3.connect('users.db')
            c = connection.cursor()
            update_point = """UPDATE users
                            SET games = games + 1
                            WHERE
                            username = ?"""
            c.execute(update_point, [user1])
            update_point = """UPDATE users
                                    SET games = games + 1
                                    WHERE
                                    username = ?"""
            c.execute(update_point, [user2])
            connection.commit()
            connection.close()

    def check_for_end():
        for i in range(n):
            for j in range(n):
                if buttons[i][j]['text'] == '':
                    return False
        return True

    def check_for_point_s(button, i, j):
        global flag
        global player_flag
        global player_one_point
        global player_two_point
        point_diff = 0
        if i > 1 and j > 1:
            if buttons[i - 1][j - 1]['text'] == 'O' and buttons[i - 2][j - 2]['text'] == 'S':
                buttons[i - 1][j - 1].config(bg=flag)
                buttons[i - 2][j - 2].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1
        if i > 1:
            if buttons[i - 1][j]['text'] == 'O' and buttons[i - 2][j]['text'] == 'S':
                buttons[i - 1][j].config(bg=flag)
                buttons[i - 2][j].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1

        if j > 1:
            if buttons[i][j - 1]['text'] == 'O' and buttons[i][j - 2]['text'] == 'S':
                buttons[i][j - 1].config(bg=flag)
                buttons[i][j - 2].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1

        if i > 1 and j < n - 2:
            if buttons[i - 1][j + 1]['text'] == 'O' and buttons[i - 2][j + 2]['text'] == 'S':
                buttons[i - 1][j + 1].config(bg=flag)
                buttons[i - 2][j + 2].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1

        if i < n - 2 and j < n - 2:
            if buttons[i + 1][j + 1]['text'] == 'O' and buttons[i + 2][j + 2]['text'] == 'S':
                buttons[i + 1][j + 1].config(bg=flag)
                buttons[i + 2][j + 2].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1

        if j < n - 2:
            if buttons[i][j + 1]['text'] == 'O' and buttons[i][j + 2]['text'] == 'S':
                buttons[i][j + 1].config(bg=flag)
                buttons[i][j + 2].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1

        if i < n - 2:
            if buttons[i + 1][j]['text'] == 'O' and buttons[i + 2][j]['text'] == 'S':
                buttons[i + 1][j].config(bg=flag)
                buttons[i + 2][j].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1

        if i < n - 2 and j > 1:
            if buttons[i + 1][j - 1]['text'] == 'O' and buttons[i + 2][j - 2]['text'] == 'S':
                buttons[i + 1][j - 1].config(bg=flag)
                buttons[i + 2][j - 2].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1
        if point_diff == 0:
            player_flag = not player_flag
            if player_flag is True:
                turn['text'] = user1
                flag = player_one_color
            else:
                turn['text'] = user2
                flag = player_two_color
        else:
            if player_flag:
                player_one_point += point_diff
            else:
                player_two_point += point_diff
            second_user_point['text'] = player_two_point
            first_user_point['text'] = player_one_point

        if check_for_end():
            update_db_points()
            tk.destroy()
            if player_two_point > player_one_point:
                ms.showinfo('GG WP', "Player Two wins")
            elif player_two_point < player_one_point:
                ms.showinfo('GG WP',"Player One wins")
            else:
                ms.showinfo('GG WP', "Tie")

    def check_for_point_o(button, i, j):
        global flag
        global player_flag
        global player_one_point
        global player_two_point
        point_diff = 0
        if 0 < i < n - 1:
            if buttons[i - 1][j]['text'] == 'S' and buttons[i + 1][j]['text'] == 'S':
                buttons[i - 1][j].config(bg=flag)
                buttons[i + 1][j].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1
        if 0 < j < n - 1:
            if buttons[i][j - 1]['text'] == 'S' and buttons[i][j + 1]['text'] == 'S':
                buttons[i][j - 1].config(bg=flag)
                buttons[i][j + 1].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1
        if 0 < i < n - 1 and 0 < j < n - 1:
            if buttons[i - 1][j - 1]['text'] == 'S' and buttons[i + 1][j + 1]['text'] == 'S':
                buttons[i - 1][j - 1].config(bg=flag)
                buttons[i + 1][j + 1].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1
            if buttons[i - 1][j + 1]['text'] == 'S' and buttons[i + 1][j - 1]['text'] == 'S':
                buttons[i - 1][j + 1].config(bg=flag)
                buttons[i + 1][j - 1].config(bg=flag)
                buttons[i][j].config(bg=flag)
                point_diff += 1
        if point_diff == 0:
            player_flag = not player_flag
            if player_flag is True:
                turn['text'] = user1
                flag = player_one_color
            else:
                turn['text'] = user2
                flag = player_two_color
        else:
            if player_flag:
                player_one_point += point_diff
            else:
                player_two_point += point_diff
            second_user_point['text'] = player_two_point
            first_user_point['text'] = player_one_point

        if check_for_end():
            update_db_points()
            tk.destroy()
            if player_two_point > player_one_point:
                ms.showinfo('GG WP', "Player Two wins")
            elif player_two_point < player_one_point:
                ms.showinfo('GG WP', "Player One wins")
            else:
                ms.showinfo('GG WP', "Tie")

    def S(event, args):
        args[0].config(text='S', font='bold')
        args[0].unbind('<Button-3>')
        args[0].unbind('<Button-1>')
        print(args[1], args[2])
        check_for_point_s(args[0], args[1], args[2])

    def O(event, args):
        args[0].config(text='O', font='bold')
        args[0].unbind('<Button-3>')
        args[0].unbind('<Button-1>')
        print(args[1], args[2])
        check_for_point_o(args[0], args[1], args[2])

    def disable_button(n):
        for i in range(1, n + 1):
            buttons.append([])
            for j in range(1, n + 1):
                lb = Button(tk, text='', bg='white', state='disabled')
                buttons[-1].append(lb)

                lb.bind('<Button-1>', lambda event, arg=[lb, i - 1, j - 1]: S(event, arg))
                lb.bind('<Button-3>', lambda event, arg=[lb, i - 1, j - 1]: O(event, arg))

                # lb.config()
                lb.place(x=150 + (i - 1) * 500 / n, y=150 + (j - 1) * 500 / n, width=int(500 / n), height=int(500 / n))
                # lb.pack()

    disable_button(n)

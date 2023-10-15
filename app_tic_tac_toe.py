# from tkinter import *
# from tkinter.ttk import *
#
#
# def change_button_11():
#     # button_11.config(text="X")
#     global flag
#     if flag:
#         button_11.config(text="X")
#         flag = False
#     else:
#         button_11.config(text="O")
#         flag = True
#
#
# def change_button_21():
#     # button_21.config(text="X")
#     global flag
#     if flag:
#         button_21.config(text="X")
#         flag = False
#     else:
#         button_21.config(text="O")
#         flag = True
#
#
# def change_button_12():
#     # button_12.config(text="X")
#     global flag
#     if flag:
#         button_12.config(text="X")
#         flag = False
#     else:
#         button_12.config(text="O")
#         flag = True
#
#
# def change_button_22():
#     # button_22.config(text="X")
#     global flag
#     if flag:
#         button_22.config(text="X")
#         flag = False
#     else:
#         button_22.config(text="O")
#         flag = True
#
#
# root = Tk()
# root.title("Tic-tac-toy v.03")
# flag = True
# button_11 = Button(root, command=change_button_11)
# button_11.grid(column=1, row=1, ipady=22)
# button_21 = Button(root, command=change_button_21)
# button_21.grid(column=2, row=1, ipady=22)
# button_12 = Button(root, command=change_button_12)
# button_12.grid(column=1, row=2, ipady=22)
# button_22 = Button(root, command=change_button_22)
# button_22.grid(column=2, row=2, ipady=22)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def change_button_11():
#     print(button_11["text"] == "")
#     global flag
#     if not button_11["text"]:
#         if flag:
#             button_11.config(text="X")
#             # flag = False
#             # flag = not flag
#         else:
#             button_11.config(text="O")
#             # flag = True
#             # flag = not flag
#         flag = not flag
#
#
# def change_button_21():
#     print(button_21["text"] == "")
#     global flag
#     if not button_21["text"] and flag:
#         button_21.config(text="X")
#         flag = not flag
#     elif not button_21["text"] and not flag:
#         button_21.config(text="O")
#         flag = not flag
#
#
# def change_button_12():
#     global flag
#     if not button_12["text"]:
#         if flag:
#             button_12.config(text="X")
#         else:
#             button_12.config(text="O")
#         flag = not flag
#
#
# def change_button_22():
#     global flag
#     if not button_22["text"]:
#         if flag:
#             button_22.config(text="X")
#         else:
#             button_22.config(text="O")
#
#
# def start_new_game():
#     button_11.config(text="")
#     button_21.config(text="")
#     button_12.config(text="")
#     button_22.config(text="")
#
#
# root = Tk()
# root.title("Tic-tac-toy v.04")
# flag = True
# button_11 = Button(root, command=change_button_11)
# button_11.grid(column=1, row=1, ipady=23)
# button_21 = Button(root, command=change_button_21)
# button_21.grid(column=2, row=1, ipady=23)
# button_12 = Button(root, command=change_button_12)
# button_12.grid(column=1, row=2, ipady=23)
# button_22 = Button(root, command=change_button_22)
# button_22.grid(column=2, row=2, ipady=23)
# button_new_game = Button(root, text="NEW GAME", command=start_new_game)
# button_new_game.grid(column=1, row=3, columnspan=2, ipadx=40)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def change_button_11():
#     global flag
#     if not button_11["text"]:
#         if flag:
#             button_11.config(text="X")
#             # flag = False
#             # flag = not flag
#         else:
#             button_11.config(text="O")
#             # flag = True
#             # flag = not flag
#         flag = not flag
#         check_winner()
#
#
# def change_button_21():
#     global flag
#     if not button_21["text"] and flag:
#         button_21.config(text="X")
#         flag = not flag
#     elif not button_21["text"] and not flag:
#         button_21.config(text="O")
#         flag = not flag
#     check_winner()
#
#
# def change_button_12():
#     global flag
#     if not button_12["text"]:
#         if flag:
#             button_12.config(text="X")
#         else:
#             button_12.config(text="O")
#         flag = not flag
#         check_winner()
#
#
# def change_button_22():
#     global flag
#     if not button_22["text"]:
#         if flag:
#             button_22.config(text="X")
#         else:
#             button_22.config(text="O")
#         flag = not flag
#         check_winner()
#
#
# def start_new_game():
#     button_11.config(text="")
#     button_21.config(text="")
#     button_12.config(text="")
#     button_22.config(text="")
#
#
# def check_winner():
#     print("Row 1:", button_11["text"] == "X" and button_21["text"] == "X"
#           or button_11["text"] == "O" and button_21["text"] == "O")
#     print("Row 2:", button_12["text"] == "X" and button_21["text"] == "X"
#           or button_12["text"] == "O" and button_21["text"] == "O")
#     print("Column 1:", button_11["text"] == "X" and button_12["text"] == "X"
#           or button_11["text"] == "O" and button_12["text"] == "O")
#     print("Column 2:", button_21["text"] == "X" and button_22["text"] == "X"
#           or button_21["text"] == "O" and button_22["text"] == "O")
#     print("Diagonal 11-22:", button_11["text"] == "X" and button_22["text"] == "X"
#           or button_11["text"] == "O" and button_22["text"] == "O")
#     print("Diagonal 12-21:", button_12["text"] == "X" and button_21["text"] == "X"
#           or button_12["text"] == "O" and button_21["text"] == "O")
#
#
# root = Tk()
# root.title("Tic-tac-toy v.04")
# flag = True
# button_11 = Button(root, command=change_button_11)
# button_11.grid(column=1, row=1, ipady=23)
# button_21 = Button(root, command=change_button_21)
# button_21.grid(column=2, row=1, ipady=23)
# button_12 = Button(root, command=change_button_12)
# button_12.grid(column=1, row=2, ipady=23)
# button_22 = Button(root, command=change_button_22)
# button_22.grid(column=2, row=2, ipady=23)
# button_new_game = Button(root, text="NEW GAME", command=start_new_game)
# button_new_game.grid(column=1, row=3, columnspan=2, ipadx=40)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def change_button_11():
#     global flag
#     if not button_11["text"]:
#         if flag:
#             button_11.config(text="X")
#             # flag = False
#             # flag = not flag
#         else:
#             button_11.config(text="O")
#             # flag = True
#             # flag = not flag
#         flag = not flag
#         # check_winner()
#         check_winner_xo()
#
#
# def change_button_21():
#     global flag
#     if not button_21["text"] and flag:
#         button_21.config(text="X")
#         flag = not flag
#     elif not button_21["text"] and not flag:
#         button_21.config(text="O")
#         flag = not flag
#     # check_winner()
#     check_winner_xo()
#
#
# def change_button_12():
#     global flag
#     if not button_12["text"]:
#         if flag:
#             button_12.config(text="X")
#         else:
#             button_12.config(text="O")
#         flag = not flag
#         # check_winner()
#         check_winner_xo()
#
#
# def change_button_22():
#     global flag
#     if not button_22["text"]:
#         if flag:
#             button_22.config(text="X")
#         else:
#             button_22.config(text="O")
#         flag = not flag
#         # check_winner()
#         check_winner_xo()
#
#
# def start_new_game():
#     button_11.config(text="")
#     button_21.config(text="")
#     button_12.config(text="")
#     button_22.config(text="")
#
#
# def check_winner():
#     print("Row 1:", button_11["text"] == button_21["text"] == "X"
#           or button_11["text"] == button_21["text"] == "O")
#     print("Row 2:", button_12["text"] == "X" and button_22["text"] == "X"
#           or button_12["text"] == "O" and button_22["text"] == "O")
#     print("Column 1:", button_11["text"] == "X" and button_12["text"] == "X"
#           or button_11["text"] == "O" and button_12["text"] == "O")
#     print("Column 2:", button_21["text"] == "X" and button_22["text"] == "X"
#           or button_21["text"] == "O" and button_22["text"] == "O")
#     print("Diagonal 11-22:", button_11["text"] == "X" and button_22["text"] == "X"
#           or button_11["text"] == "O" and button_22["text"] == "O")
#     print("Diagonal 12-21:", button_12["text"] == "X" and button_21["text"] == "X"
#           or button_12["text"] == "O" and button_21["text"] == "O")
#
#
# def check_winner_xo():
#     if button_11["text"] == "X" and button_21["text"] == "X"\
#             or button_12["text"] == "X" and button_22["text"] == "X"\
#             or button_11["text"] == "X" and button_12["text"] == "X"\
#             or button_21["text"] == "X" and button_22["text"] == "X"\
#             or button_11["text"] == "X" and button_22["text"] == "X"\
#             or button_12["text"] == "X" and button_21["text"] == "X":
#         print("X-won!")
#
#     elif button_11["text"] == "O" and button_21["text"] == "O"\
#             or button_12["text"] == "O" and button_22["text"] == "O"\
#             or button_11["text"] == "O" and button_12["text"] == "O"\
#             or button_21["text"] == "O" and button_22["text"] == "O"\
#             or button_11["text"] == "O" and button_22["text"] == "O"\
#             or button_12["text"] == "O" and button_21["text"] == "O":
#         print("O-won!")
#
#
# root = Tk()
# root.title("Tic-tac-toy v.05")
# flag = True
# button_11 = Button(root, command=change_button_11)
# button_11.grid(column=1, row=1, ipady=23)
# button_21 = Button(root, command=change_button_21)
# button_21.grid(column=2, row=1, ipady=23)
# button_12 = Button(root, command=change_button_12)
# button_12.grid(column=1, row=2, ipady=23)
# button_22 = Button(root, command=change_button_22)
# button_22.grid(column=2, row=2, ipady=23)
# button_new_game = Button(root, text="NEW GAME", command=start_new_game)
# button_new_game.grid(column=1, row=3, columnspan=2, ipadx=40)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def change_button_11():
#     global flag
#     if not button_11["text"]:
#         if flag:
#             button_11.config(text="X")
#             # flag = False
#             # flag = not flag
#         else:
#             button_11.config(text="O")
#             # flag = True
#             # flag = not flag
#         flag = not flag
#         # check_winner()
#         check_winner_xo()
#
#
# def change_button_21():
#     global flag
#     if not button_21["text"] and flag:
#         button_21.config(text="X")
#         flag = not flag
#     elif not button_21["text"] and not flag:
#         button_21.config(text="O")
#         flag = not flag
#     # check_winner()
#     check_winner_xo()
#
#
# def change_button_12():
#     global flag
#     if not button_12["text"]:
#         if flag:
#             button_12.config(text="X")
#         else:
#             button_12.config(text="O")
#         flag = not flag
#         # check_winner()
#         check_winner_xo()
#
#
# def change_button_22():
#     global flag
#     if not button_22["text"]:
#         if flag:
#             button_22.config(text="X")
#         else:
#             button_22.config(text="O")
#         flag = not flag
#         # check_winner()
#         check_winner_xo()
#
#
# def start_new_game():
#     button_11.config(text="")
#     button_21.config(text="")
#     button_12.config(text="")
#     button_22.config(text="")
#     active_buttons()
#
#
# def check_winner():
#     print("Row 1:", button_11["text"] == button_21["text"] == "X"
#           or button_11["text"] == button_21["text"] == "O")
#     print("Row 2:", button_12["text"] == "X" and button_22["text"] == "X"
#           or button_12["text"] == "O" and button_22["text"] == "O")
#     print("Column 1:", button_11["text"] == "X" and button_12["text"] == "X"
#           or button_11["text"] == "O" and button_12["text"] == "O")
#     print("Column 2:", button_21["text"] == "X" and button_22["text"] == "X"
#           or button_21["text"] == "O" and button_22["text"] == "O")
#     print("Diagonal 11-22:", button_11["text"] == "X" and button_22["text"] == "X"
#           or button_11["text"] == "O" and button_22["text"] == "O")
#     print("Diagonal 12-21:", button_12["text"] == "X" and button_21["text"] == "X"
#           or button_12["text"] == "O" and button_21["text"] == "O")
#
#
# def check_winner_xo():
#     if button_11["text"] == "X" and button_21["text"] == "X"\
#             or button_12["text"] == "X" and button_22["text"] == "X"\
#             or button_11["text"] == "X" and button_12["text"] == "X"\
#             or button_21["text"] == "X" and button_22["text"] == "X"\
#             or button_11["text"] == "X" and button_22["text"] == "X"\
#             or button_12["text"] == "X" and button_21["text"] == "X":
#         print("X-won!")
#         block_buttons()
#
#     elif button_11["text"] == "O" and button_21["text"] == "O"\
#             or button_12["text"] == "O" and button_22["text"] == "O"\
#             or button_11["text"] == "O" and button_12["text"] == "O"\
#             or button_21["text"] == "O" and button_22["text"] == "O"\
#             or button_11["text"] == "O" and button_22["text"] == "O"\
#             or button_12["text"] == "O" and button_21["text"] == "O":
#         print("O-won!")
#         block_buttons()
#
#
# def block_buttons():
#     button_11["state"] = "disable"
#     button_21["state"] = "disable"
#     button_12["state"] = "disable"
#     button_22["state"] = "disable"
#
#
# def active_buttons():
#     button_11["state"] = "normal"
#     button_21["state"] = "normal"
#     button_12["state"] = "normal"
#     button_22["state"] = "normal"
#
#
# root = Tk()
# root.title("Tic-tac-toy v.09")
# flag = True
# button_11 = Button(root, command=change_button_11)
# button_11.grid(column=1, row=1, ipady=23)
# button_21 = Button(root, command=change_button_21)
# button_21.grid(column=2, row=1, ipady=23)
# button_12 = Button(root, command=change_button_12)
# button_12.grid(column=1, row=2, ipady=23)
# button_22 = Button(root, command=change_button_22)
# button_22.grid(column=2, row=2, ipady=23)
# button_new_game = Button(root, text="NEW GAME", command=start_new_game)
# button_new_game.grid(column=1, row=3, columnspan=2, ipadx=40)
# root.mainloop()


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def change_button_11():
    global flag
    if not button_11["text"]:
        if flag:
            button_11.config(text="X")
        else:
            button_11.config(text="O")
        flag = not flag
        check_winner_xo()


def change_button_21():
    global flag
    if not button_21["text"] and flag:
        button_21.config(text="X")
        flag = not flag
    elif not button_21["text"] and not flag:
        button_21.config(text="O")
        flag = not flag
    check_winner_xo()


def change_button_31():
    global flag
    if not button_31["text"] and flag:
        button_31.config(text="X")
        flag = not flag
    elif not button_31["text"] and not flag:
        button_31.config(text="O")
        flag = not flag
    check_winner_xo()


def change_button_12():
    global flag
    if not button_12["text"]:
        if flag:
            button_12.config(text="X")
        else:
            button_12.config(text="O")
        flag = not flag
        check_winner_xo()


def change_button_22():
    global flag
    if not button_22["text"]:
        if flag:
            button_22.config(text="X")
        else:
            button_22.config(text="O")
        flag = not flag
        check_winner_xo()


def change_button_32():
    global flag
    if not button_32["text"]:
        if flag:
            button_32.config(text="X")
        else:
            button_32.config(text="O")
        flag = not flag
        check_winner_xo()


def change_button_13():
    global flag
    if not button_13["text"]:
        if flag:
            button_13.config(text="X")
        else:
            button_13.config(text="O")
        flag = not flag
        check_winner_xo()


def change_button_23():
    global flag
    if not button_23["text"]:
        if flag:
            button_23.config(text="X")
        else:
            button_23.config(text="O")
        flag = not flag
        check_winner_xo()


def change_button_33():
    global flag
    if not button_33["text"]:
        if flag:
            button_33.config(text="X")
        else:
            button_33.config(text="O")
        flag = not flag
        check_winner_xo()


def start_new_game():
    button_11.config(text="")
    button_21.config(text="")
    button_31.config(text="")
    button_12.config(text="")
    button_22.config(text="")
    button_32.config(text="")
    button_13.config(text="")
    button_23.config(text="")
    button_33.config(text="")
    active_buttons()


def check_winner_xo():
    global x_wins, o_wins, draw
    if button_11["text"] == button_21["text"] == button_31["text"] == "X"\
            or button_12["text"] == button_22["text"] == button_32["text"] == "X"\
            or button_13["text"] == button_23["text"] == button_33["text"] == "X"\
            or button_11["text"] == button_12["text"] == button_13["text"] == "X"\
            or button_21["text"] == button_22["text"] == button_23["text"] == "X"\
            or button_31["text"] == button_32["text"] == button_33["text"] == "X"\
            or button_11["text"] == button_22["text"] == button_33["text"] == "X"\
            or button_13["text"] == button_22["text"] == button_31["text"] == "X":
        x_wins = x_wins + 1
        messagebox.showinfo("Who wins?", "X-won!")
        block_buttons()

    elif button_11["text"] == button_21["text"] == button_31["text"] == "O"\
            or button_12["text"] == button_22["text"] == button_32["text"] == "O"\
            or button_13["text"] == button_23["text"] == button_33["text"] == "O"\
            or button_11["text"] == button_12["text"] == button_13["text"] == "O"\
            or button_21["text"] == button_22["text"] == button_23["text"] == "O"\
            or button_31["text"] == button_32["text"] == button_33["text"] == "O"\
            or button_11["text"] == button_22["text"] == button_33["text"] == "O"\
            or button_13["text"] == button_22["text"] == button_31["text"] == "O":
        o_wins = o_wins + 1
        messagebox.showinfo("Who wins?", "O-won!")
        block_buttons()

    elif button_11["text"] and button_21["text"] and button_31["text"] and\
            button_12["text"] and button_22["text"] and button_32["text"] and\
            button_13["text"] and button_23["text"] and button_33["text"]:
        draw = draw + 1
        messagebox.showinfo("Who wins?", "Draw!")
        block_buttons()
    count_result()


def block_buttons():
    button_11["state"] = "disable"
    button_21["state"] = "disable"
    button_31["state"] = "disable"
    button_12["state"] = "disable"
    button_22["state"] = "disable"
    button_32["state"] = "disable"
    button_13["state"] = "disable"
    button_23["state"] = "disable"
    button_33["state"] = "disable"


def active_buttons():
    button_11["state"] = "normal"
    button_21["state"] = "normal"
    button_31["state"] = "normal"
    button_12["state"] = "normal"
    button_22["state"] = "normal"
    button_32["state"] = "normal"
    button_13["state"] = "normal"
    button_23["state"] = "normal"
    button_33["state"] = "normal"


def count_result():
    text.delete(1.0, END)
    text.insert(END, f"X's victories: {x_wins}\nO's victories: {o_wins}\nDraws: {draw}")


root = Tk()
root.title("Tic-tac-toy v 3.10")
flag = True
x_wins = 0
o_wins = 0
draw = 0
button_11 = Button(root, command=change_button_11)
button_11.grid(column=1, row=1, ipady=23)
button_21 = Button(root, command=change_button_21)
button_21.grid(column=2, row=1, ipady=23)
button_31 = Button(root, command=change_button_31)
button_31.grid(column=3, row=1, ipady=23)
button_12 = Button(root, command=change_button_12)
button_12.grid(column=1, row=2, ipady=23)
button_22 = Button(root, command=change_button_22)
button_22.grid(column=2, row=2, ipady=23)
button_32 = Button(root, command=change_button_32)
button_32.grid(column=3, row=2, ipady=23)
button_13 = Button(root, command=change_button_13)
button_13.grid(column=1, row=3, ipady=23)
button_23 = Button(root, command=change_button_23)
button_23.grid(column=2, row=3, ipady=23)
button_33 = Button(root, command=change_button_33)
button_33.grid(column=3, row=3, ipady=23)
button_new_game = Button(root, text="NEW GAME", command=start_new_game)
button_new_game.grid(column=1, row=4, columnspan=3, ipadx=75)
text = Text(root, height=10, width=20)
text.grid(row=0, column=4, rowspan=5, sticky=NSEW)
root.mainloop()
